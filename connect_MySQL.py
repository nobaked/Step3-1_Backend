from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 環境変数の読み込み（.envファイルを使う場合）
load_dotenv()

# データベース接続情報の取得
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_SSL_CA = os.getenv('DB_SSL_CA')  # 例: './cert/DigiCertGlobalRootCA.crt.pem'

# データベースURL（SSL情報はここに入れない）
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemyエンジンの作成（SSL CAはconnect_argsで渡す）
engine = create_engine(
    DATABASE_URL,
    echo=True,  # ログを出力（開発中はTrue、本番ではFalseでもOK）
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args={
        "ssl_ca": DB_SSL_CA
    }
)
