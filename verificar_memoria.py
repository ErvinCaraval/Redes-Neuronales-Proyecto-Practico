#!/usr/bin/env python3
"""Script para verificar disponibilidad de memoria y cargas de datos antes de ejecutar notebook"""

import os
import sys
import psutil
import numpy as np

# Configuración
IMG_SIZE_MLP = 128
BATCH_SIZE = 32
NUM_CLASSES = 10
base_dir = "dataset"

def count_images():
    """Contar imágenes en el dataset"""
    counts = {}
    for split in ['train', 'val', 'test']:
        split_dir = os.path.join(base_dir, split)
        total = 0
        for class_name in sorted(os.listdir(split_dir)):
            class_dir = os.path.join(split_dir, class_name)
            count = len([f for f in os.listdir(class_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
            total += count
        counts[split] = total
    return counts

def estimate_memory(img_counts):
    """Estimar memoria requerida en GB"""
    bytes_per_image = IMG_SIZE_MLP * IMG_SIZE_MLP * 3 * 4  # float32
    memory_per_split = {}
    total = 0
    
    for split, count in img_counts.items():
        memory_gb = (count * bytes_per_image) / 1e9
        memory_per_split[split] = memory_gb
        total += memory_gb
    
    return memory_per_split, total

def main():
    print("\n" + "="*70)
    print("DIAGNÓSTICO DE MEMORIA - PROYECTO MAÍZ")
    print("="*70)
    
    # Estado del sistema
    memory = psutil.virtual_memory()
    print(f"\n📊 ESTADO DEL SISTEMA:")
    print(f"  RAM total: {memory.total / 1e9:.2f} GB")
    print(f"  RAM usada: {memory.used / 1e9:.2f} GB ({memory.percent:.1f}%)")
    print(f"  RAM disponible: {memory.available / 1e9:.2f} GB")
    
    # Configuración del modelo
    pixels_per_image = IMG_SIZE_MLP * IMG_SIZE_MLP * 3
    print(f"\n🖼️  CONFIGURACIÓN DEL MODELO MLP:")
    print(f"  Tamaño imagen: {IMG_SIZE_MLP}x{IMG_SIZE_MLP}x3 = {pixels_per_image} píxeles")
    print(f"  Bytes por imagen: {pixels_per_image * 4 / 1e6:.2f} MB (float32)")
    
    # Dataset
    img_counts = count_images()
    memory_reqs, total_memory = estimate_memory(img_counts)
    
    print(f"\n📁 DATASET:")
    for split, count in img_counts.items():
        print(f"  {split.capitalize()}: {count} imágenes → {memory_reqs[split]:.3f} GB")
    
    print(f"\n💾 MEMORIA REQUERIDA (solo datos):")
    print(f"  Total: {total_memory:.3f} GB")
    
    # Validación
    print(f"\n✅ VALIDACIÓN:")
    
    if memory.available / 1e9 < total_memory:
        print(f"  ⚠️  ALERTA: RAM disponible ({memory.available / 1e9:.2f} GB) < memoria requerida ({total_memory:.3f} GB)")
        print(f"     → Cierra otras aplicaciones antes de ejecutar")
        return False
    else:
        disponible = memory.available / 1e9 - total_memory
        print(f"  ✓ RAM disponible después de carga: {disponible:.2f} GB (OK)")
    
    if memory.percent > 80:
        print(f"  ⚠️  ALERTA: Sistema con alto uso de RAM ({memory.percent:.1f}%)")
        print(f"     → Se recomienda cerrar aplicaciones")
        return False
    
    print(f"  ✓ Uso de RAM del sistema: {memory.percent:.1f}% (OK)")
    print(f"\n{'='*70}")
    print("✅ Sistema APTO para ejecutar el notebook")
    print(f"{'='*70}\n")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
