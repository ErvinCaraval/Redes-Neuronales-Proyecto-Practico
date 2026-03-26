#  Proyecto: Entrega 1 - Clasificación MLP vs Deep Learning

##  Descripción del Proyecto

Clasificación de enfermedades de caña de azúcar utilizando:
- **MLP (Perceptrón Multicapa)**: Red neuronal tradicional con 234M parámetros
- **Deep Learning (EfficientNetB0)**: Transfer Learning con pesos pre-entrenados en ImageNet
- **Comparación de Desempeño**: Métricas, visualizaciones y análisis crítico

**Clases**: 10 enfermedades del caña de azúcar (Carbon, Roya, Sanas, Secas, etc.)

---

##  Requisitos del Sistema

- **Python**: 3.8 o superior
- **pip**: Administrador de paquetes de Python
- **Espacio en disco**: ~2GB (para TensorFlow y dataset)
- **RAM mínima**: 4GB (8GB recomendado)

---

##  Estructura del Proyecto

```
Redes-Neuronales-Proyecto-Practico/
├── Entrega_1_MLP_vs_DeepLearning.ipynb       # Notebook principal
├── entrenamiento_efficientnet.ipynb           # Entrenamiento de EfficientNetB0
├── dividir_datos.py                           # Script para dividir dataset
├── requirements.txt                           # Dependencias del proyecto
├── README.md                                  # Este archivo
├── .gitignore                                 # Configuración de Git
│
├──  MODELOS (raíz - se generan durante ejecución)
├── modelo_EfficientNetB0.keras                # Modelo Deep Learning (~50MB)
├── mlp_best_model.keras                       # Mejor modelo MLP (~200MB)
│
├── outputs/                                   # Carpeta de salidas organizadas
│   ├── graphics/
│   │   ├── mlp_early_stopping_effect.png      # Gráfica de Early Stopping
│   │   ├── comparacion_metricas.png           # Comparación MLP vs DL
│   │   └── metricas_por_clase.png             # Métricas por clase
│   └── logs/                                  # Logs de ejecución (si existen)
│
└── dataset/
    ├── train/        # 70% imágenes de entrenamiento
    ├── val/          # 15% imágenes de validación
    └── test/         # 15% imágenes de prueba
        └── [10 carpetas de clases de enfermedades]
```

---

##  Configuración del Entorno Virtual

### **OPCIÓN 1: LINUX/MAC**

#### 1️ Crear el entorno virtual

```bash
python3 -m venv venv
```

#### 2️ Activar el entorno virtual

```bash
source venv/bin/activate
```

**¿Funciona?** Deberías ver `(venv)` al inicio de la línea en la terminal.

#### 3️ Actualizar pip

```bash
pip install --upgrade pip
```

#### 4️ Instalar dependencias

```bash
pip install -r requirements.txt
```

#### 5️ Verificar instalación

```bash
python -c "import tensorflow as tf; print(f'TensorFlow: {tf.__version__}')"
```

#### 6️ Lanzar Jupyter

```bash
jupyter notebook
```

Esto abrirá Jupyter en `http://localhost:8888`

---

### **OPCIÓN 2: WINDOWS**

#### 1️ Crear el entorno virtual

Abre **PowerShell** o **Símbolo del Sistema** en la carpeta del proyecto:

```bash
python -m venv venv
```

#### 2️ Activar el entorno virtual

En **PowerShell**:
```bash
.\venv\Scripts\Activate.ps1
```

En **Símbolo del Sistema (cmd)**:
```bash
venv\Scripts\activate.bat
```

**¿Funciona?** Deberías ver `(venv)` al inicio de la línea.

#### 3️ Actualizar pip

```bash
python -m pip install --upgrade pip
```

#### 4️ Instalar dependencias

```bash
pip install -r requirements.txt
```

Esto puede tomar **5-10 minutos** (TensorFlow es grande).

#### 5️ Verificar instalación

```bash
python -c "import tensorflow as tf; print(f'TensorFlow: {tf.__version__}')"
```

#### 6️ Lanzar Jupyter

```bash
jupyter notebook
```

---

##  Cómo Ejecutar los Notebooks

### **Ejecutar Entrega 1**

1. Con Jupyter abierto, abre `Entrega_1_MLP_vs_DeepLearning.ipynb`
2. Ejecuta las celdas **en orden** (Shift + Enter o botón ▶ Play)
3. **Tiempo estimado**: ~35 minutos (primera vez), ~20 minutos (sin entrenar)

### **Puntos Críticos de Ejecución**

| Celda | Operación | Tiempo |
|-------|-----------|--------|
| 1-4 | Imports y carga de datos | ~3 min |
| 5-6 | Entrenamiento MLP | ~10 min |
| 7 | Carga/Entrenamiento EfficientNetB0 | ~15 min (si no existe modelo) |
| 8-14 | Evaluación y análisis | ~2 min |

---

##  9. Estrategias y parámetros de entrenamiento (Resumen solicitado)

### Notebook `Entrega_1_MLP_vs_DeepLearning.ipynb`
- Dataset: `dataset/train`, `dataset/val`, `dataset/test` (10 clases)
- Tamaño de imagen: 128x128 para ambas arquitecturas
- MLP:
  - Entrada: vector aplanado de 128x128x3 = 49.152 features
  - Capas: Dense(256)->BatchNorm->Dropout(0.4), Dense(128)->BatchNorm->Dropout(0.3), Dense(64)->Dropout(0.3), Softmax(10)
  - Optimizer: Adam lr=0.001
  - Loss: categorical_crossentropy
  - Batch size: 32
  - Epochs: max 25 + EarlyStopping(patience=10, restore_best_weights=True)
  - Callbacks: EarlyStopping, ReduceLROnPlateau(factor=0.5, patience=4, min_lr=1e-7), ModelCheckpoint('mlp_best_model.keras')
  - Regularización: dropout + batch normalization + reducción de arquitectura
- EfficientNetB0 (cargado o entrenado desde `entrenamiento_efficientnet.ipynb`):
  - Base sin top con pesos ImageNet, `base_model.trainable=False`
  - Capas adicionales: GlobalAveragePooling2D, Dense(128, relu), Dropout(0.5), Dense(10 softmax)
  - Optimizer: Adam (default)
  - Loss: categorical_crossentropy
  - Epochs: 5
  - Batch size: 32
  - Preprocesamiento: `preprocess_input` + augmentation en train (flip horiz/vert, rotación 30, brillo 0.8-1.2, zoom 0.1)
  - Validación/Test sin augmentación
- Métricas evaluadas:
  - accuracy, precision, recall, f1-score, confusion matrix, classification report

### Notebook `entrenamiento_efficientnet.ipynb`
- Parámetros globales:
  - IMG_SIZE=128, BATCH_SIZE=32, EPOCHS=5, NUM_CLASSES=10
- Arquitectura y transfer learning:
  - EfficientNetB0 preentrenado (imagenet), top excluido, base congelada
  - Añade pooling + Dense(128) + Dropout(0.5) + Dense(10 softmax)
- Entrenamiento directos:
  - history = model.fit(train_generator, validation_data=val_generator, epochs=EPOCHS)
- Salida: modelo guardado en `modelo_EfficientNetB0.keras`

### Estrategias generales aplicadas (en ambos notebooks)
- Reducción de tamaño de imagen para memoria y velocidad.
- Aumento de datos en entrenamiento del modelo DL para robustez.
- Early stopping y learning rate dinámico en MLP para evitar overfitting.
- Almacenamiento del mejor modelo y calculo de métricas robustas para comparación.

---

##  Troubleshooting (Solución de Problemas)

###  Error: `python: command not found`

**Solución**: En Windows, usa `python`. En Mac/Linux, intenta `python3`.

```bash
# Linux/Mac
python3 --version

# Windows
python --version
```

---

###  Error: `ModuleNotFoundError: No module named 'tensorflow'`

**Solución**: Asegúrate de que el entorno virtual está **activado**:

```bash
# Linux/Mac
source venv/bin/activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (cmd)
venv\Scripts\activate.bat
```

---

###  Error: `Permission denied` en Linux

**Solución**: Dale permisos a los scripts:

```bash
chmod +x venv/bin/activate
```

---

###  Entorno virtual lento o con problemas

**Solución**: Recrea desde cero:

```bash
# Desactiva primero
deactivate

# Elimina carpeta venv
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows

# Recrea desde el paso 1
python3 -m venv venv
```

---

###  TensorFlow tarda mucho en instalar

**Es normal.** TensorFlow es un paquete grande (~500MB). Paciencia de 5-10 minutos.

---

##  Verificación Final

Una vez configurado, ejecuta esto para confirmar que todo funciona:

```bash
python << 'EOF'
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import jupyter

print("✓ TensorFlow:", tf.__version__)
print("✓ NumPy:", np.__version__)
print("✓ Jupyter instalado")
print("\n Entorno listo para ejecutar notebooks")
EOF
```

---

##  Salidas Esperadas

Al ejecutar `Entrega_1_MLP_vs_DeepLearning.ipynb`:

### **Modelos (Raíz del Proyecto)**
- `modelo_EfficientNetB0.keras` - Modelo de Deep Learning entrenado (~50MB)
- `mlp_best_model.keras` - Mejor modelo MLP guardado por Early Stopping (~200MB)

### **Gráficas Generadas (outputs/graphics/)**
1. **mlp_early_stopping_effect.png** - Visualización del efecto de Early Stopping
   - Pérdida de entrenamiento vs validación
   - Precisión de entrenamiento vs validación
   
2. **comparacion_metricas.png** - Comparación MLP vs Deep Learning
   - Barras de Accuracy, Precision, Recall, F1-Score
   - Matrices de confusión
   - Diferencia de desempeño
   
3. **metricas_por_clase.png** - Análisis por clase de enfermedad
   - Precision, Recall y F1-Score para cada una de las 10 clases
   - Comparación visual entre modelos

### **Reportes (Console Output)**
- Métricas generales (Accuracy, Precision, Recall, F1-Score)
- Análisis de Early Stopping
- Comparación crítica de desempeño
- Resumen ejecutivo

---

##  Dependencias Incluidas

| Librería | Versión | Propósito |
|----------|---------|----------|
| TensorFlow | ≥2.10.0 | Framework de Deep Learning |
| Keras | ≥2.10.0 | API para redes neuronales |
| NumPy | ≥1.21.0 | Cálculos numéricos |
| Pandas | ≥1.3.0 | Manipulación de datos |
| Matplotlib | ≥3.4.0 | Visualización |
| Seaborn | ≥0.11.0 | Gráficas avanzadas |
| Scikit-learn | ≥1.0.0 | Métricas y validación |
| Jupyter | ≥1.0.0 | Notebooks interactivos |

---

##  Próximos Pasos

1.  Configurar entorno virtual
2.  Instalar dependencias
3.  Ejecutar `Entrega_1_MLP_vs_DeepLearning.ipynb`
4.  Revisar salidas en:
    - **Modelos**: Raíz del proyecto (`*.keras`)
    - **Gráficas**: `outputs/graphics/`
5.  Generar reporte (máx 10 páginas)
6.  Crear presentación (máx 10 diapositivas)
7.  Preparar sustentación

---

##  Información de Archivos Generados

| Archivo | Ubicación | Tamaño | Descripción |
|---------|-----------|--------|------------|
| modelo_EfficientNetB0.keras | Raíz | ~50MB | Modelo DL pre-entrenado |
| mlp_best_model.keras | Raíz | ~200MB | Mejor modelo MLP (Early Stop) |
| mlp_early_stopping_effect.png | outputs/graphics/ | ~500KB | Gráfica Early Stopping |
| comparacion_metricas.png | outputs/graphics/ | ~800KB | Comparación MLP vs DL |
| metricas_por_clase.png | outputs/graphics/ | ~600KB | Análisis por clase |

**Nota**: Los archivos `.keras` se ignoran en Git (en `.gitignore`) debido a su tamaño. Las gráficas PNG se guardan en `outputs/graphics/` para fácil identificación.

---

##  Soporte

Para preguntas técnicas:
- TensorFlow: https://www.tensorflow.org/guide
- Jupyter: https://jupyter.org/
- NumPy: https://numpy.org/doc/

---

**Creado**: Marzo 2026  
**Proyecto**: Redes Neuronales - Entrega 1  
**Estado**:  LISTO PARA EJECUTAR
