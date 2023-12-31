from etl_ops import extract_from_mysql, transform_df, load_to_postgres
from connections import create_spark_session

if __name__ == "__main__":
    spark = create_spark_session()
    table = "imdb_data_final"
    df = extract_from_mysql(spark, table=table)

    apply_transform = True
    if apply_transform:
        df = transform_df(df)

    load_to_postgres(spark, df, table=table)

    spark.stop()