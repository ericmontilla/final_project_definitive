import polars as pl
from sklearn.model_selection import train_test_split
from typing import List

class HousePricePredictor:
    def __init__(self, data_path: str):
        """
        Inicializa el predictor con los datos cargados desde un archivo CSV.
        """
        try:
            # Intentar cargar el archivo CSV especificando 'NA' como valor nulo
            self.data = pl.read_csv(data_path, null_values=["NA"])  # Definir 'NA' como valor nulo
            print("Datos cargados correctamente.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            raise

    def clean_data(self):
        """
        Realiza la limpieza de datos (por ejemplo, manejo de valores nulos, conversiones, etc.).
        """
        try:
            # Paso 1: Revisar cuántos valores nulos hay antes de limpiar
            print(f"Datos antes de limpieza: {self.data.shape}")
            print(f"Valores nulos por columna:\n{self.data.null_count()}")  # Cambiado a 'null_count()'

            # Asegúrate de que las columnas nulas sean tratadas, por ejemplo, rellenar en lugar de eliminar
            # Paso 2: Rellenar valores nulos para columnas numéricas con la mediana
            numeric_columns = [col for col in self.data.columns if self.data[col].dtype in [pl.Float64, pl.Int64]]
            for col in numeric_columns:
                median_value = self.data.select(pl.median(col)).to_numpy()[0][0]
                self.data = self.data.with_columns(self.data[col].fill_null(median_value).alias(col))
                print(f"Valores nulos en {col} rellenados con la mediana.")

            # Paso 3: Rellenar valores nulos para columnas categóricas con un valor por defecto (por ejemplo, 'Desconocido')
            categorical_columns = [
                "MSZoning", "Street", "LotShape", "LandContour", "Utilities", "LotConfig",
                "LandSlope", "Neighborhood", "Condition1", "Condition2", "BldgType", "HouseStyle",
                "RoofStyle", "Exterior1st", "Exterior2nd", "MasVnrType", "Foundation",
                "Heating", "CentralAir", "GarageType", "SaleType", "SaleCondition"
            ]
            for col in categorical_columns:
                if col in self.data.columns:
                    self.data = self.data.with_columns(self.data[col].fill_null("Desconocido").alias(col))
                    print(f"Valores nulos en {col} rellenados con 'Desconocido'.")

            # Paso 4: Eliminar columnas irrelevantes
            irrelevant_columns = ["Alley", "PoolQC", "Fence", "MiscFeature"]
            self.data = self.data.drop(irrelevant_columns)

            # Verificar cuántas filas y columnas hay después de la limpieza
            print(f"Datos después de limpieza: {self.data.shape}")
            print(f"Valores nulos por columna después de la limpieza:\n{self.data.null_count()}")  # Cambiado a 'null_count()'

            print("Datos limpios correctamente.")
        except Exception as e:
            print(f"Error al limpiar los datos: {e}")
            raise

    def prepare_features(self, target_column: str = 'SalePrice', selected_predictors: List[str] = None):
        """
        Prepara las características para el entrenamiento y prueba, dividiendo en sets de entrenamiento y prueba.
        """
        try:
            # Si no se especifican las características, usar todas menos la columna objetivo
            if selected_predictors is None:
                selected_predictors = [col for col in self.data.columns if col != target_column]

            # Verificar las columnas seleccionadas antes de continuar
            print(f"Columnas seleccionadas: {selected_predictors}")

            # Separar características y la columna objetivo
            X = self.data.select(selected_predictors)
            y = self.data.select(target_column)

            # Convertir a pandas para usar con sklearn
            X = X.to_pandas()
            y = y.to_pandas()

            # Verificar cuántas filas y columnas tiene X antes de la división
            print(f"Tamaño de X antes de la división: {X.shape}")

            # Paso 2: Dividir los datos en conjuntos de entrenamiento (80%) y prueba (20%)
            if X.shape[0] > 0:  # Solo dividir si hay filas
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                print("Características preparadas y datos divididos correctamente.")
                return X_train, X_test, y_train, y_test
            else:
                print("No hay datos suficientes para dividir en train y test.")
                return None, None, None, None

        except Exception as e:
            print(f"Error al preparar las características: {e}")
            raise

# Uso del código:

data_path = 'src/real_estate_toolkit/data/input/train.csv'  # Asegúrate de poner la ruta correcta a tu archivo CSV
predictor = HousePricePredictor(data_path)

# Limpieza de los datos
predictor.clean_data()

# Preparar las características (esto también dividirá los datos en train y test)
X_train, X_test, y_train, y_test = predictor.prepare_features(target_column="SalePrice")

# Aquí puedes continuar con el entrenamiento del modelo utilizando X_train, X_test, y_train, y_test
