#  Proyecto: Entrega 1 - Clasificación MLP vs Deep Learning

##  Descripción del Proyecto

Clasificación de enfermedades de caña de azúcar utilizando:
- **MLP (Perceptrón Multicapa)**: Arquitectura profunda optimizada (~25.6M parámetros).
- **Deep Learning (EfficientNetB0)**: Transfer Learning con pesos pre-entrenados en ImageNet.
- **Comparación de Desempeño**: Evaluación exhaustiva mediante métricas y matrices de confusión.

**Clases**: 10 enfermedades del caña de azúcar (Carbon, Roya, Sanas, Secas, etc.)

---

##  Organización del Proyecto

El proyecto está estructurado de la siguiente manera para facilitar la navegación y el mantenimiento:

- `data/`: Datasets originales y procesados (divididos en `train`, `val`, `test`).
- `models/`: Archivos `.keras` con los mejores pesos guardados durante el entrenamiento.
- `notebooks/`: Cuadernos Jupyter numerados para seguir el flujo de trabajo:
  - `01_mlp_training.ipynb`: Entrenamiento del modelo MLP.
  - `02_dl_training.ipynb`: Entrenamiento del modelo EfficientNetB0.
  - `03_comparison.ipynb`: Comparación de resultados y métricas.
- `src/`: Funciones de utilidad para el preprocesamiento y carga de datos (`data_utils.py`).
- `outputs/`: Carpeta para guardar gráficas, matrices de confusión y reportes generados.
- `requirements.txt`: Lista de dependencias del proyecto.

---

##  Requisitos del Sistema

- **Python**: 3.8 o superior
- **pip**: Administrador de paquetes de Python
- **Espacio en disco**: ~2GB (para TensorFlow y dataset)
- **RAM mínima**: 4GB (8GB recomendado)

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

##  Guía de Uso

Para reproducir los resultados, sigue este orden en los notebooks:

1. **`01_mlp_training.ipynb`**: Carga los datos y entrena el Perceptrón Multicapa. El mejor modelo se guardará en `models/mlp_best_model.keras`.
2. **`02_dl_training.ipynb`**: Realiza Transfer Learning con EfficientNetB0. El mejor modelo se guardará en `models/dl_best_model.keras`.
3. **`03_comparison.ipynb`**: Carga ambos modelos guardados y genera las métricas comparativas y matrices de confusión finales.

---

