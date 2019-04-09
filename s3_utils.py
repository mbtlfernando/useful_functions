import pandas as pd
import boto3
from io import BytesIO, StringIO
import json
import pickle


debug = 0

class S3Utils:

    @staticmethod
    def read_df_from_s3_csv(bkt, path):
        try:
            s3_client = boto3.client('s3')
            obj = s3_client.get_object(Bucket=bkt, Key=path)
            df = pd.read_csv(BytesIO(obj['Body'].read()))
            return df if len(df) > 0 else None
        except Exception as e:
            if debug > 0:
                print("Encountered exception reading S3: {}".format(e))
            return None

    @staticmethod
    def read_df_from_s3_json(bkt, path):
        try:
            s3_client = boto3.client('s3')
            obj = s3_client.get_object(Bucket=bkt, Key=path)
            df = pd.read_json(BytesIO(obj['Body'].read()))
            return df if len(df) > 0 else None
        except Exception as e:
            if debug > 0:
                print("Encountered exception reading S3: {}".format(e))
            return None

    @staticmethod
    def read_dict_from_s3_json(bkt, path):
        try:
            s3_client = boto3.client('s3')
            obj = s3_client.get_object(Bucket=bkt, Key=path)
            return json.loads(obj['Body'].read().decode('utf-8'))
        except Exception as e:
            if debug > 0:
                print("Encountered exception reading S3: {}".format(e))
            return None

    @staticmethod
    def write_df_to_s3_json(bkt, path,df):
        sess = boto3.session.Session()
        s3_resource = sess.client('s3')
        try:
            s3_resource.put_object(Body=df.to_json(),Bucket=bkt, Key=path)
        except Exception as e:
            if debug > 0:
                print("Encountered exception reading S3: {}".format(e))
            return None

    @staticmethod
    def write_dict_to_s3_json(bkt, path, _dict):
        sess = boto3.session.Session()
        s3_resource = sess.client('s3')
        try:
            s3_resource.put_object(Body=json.dumps(_dict), Bucket=bkt, Key=path)
        except Exception as e:
            if debug > 0:
                print("Encountered exception reading S3: {}".format(e))
            return None

    @staticmethod
    def write_df_to_csv(bkt, path,df):
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        s3_resource = boto3.client('s3')
        s3_resource.put_object(Body=csv_buffer.getvalue(), Bucket=bkt,
                               Key=path)

    @staticmethod
    def get_items_in_path(bkt,path):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(name=bkt)
        lst_items = [x.key for x in bucket.objects.filter(Prefix=path)]
        return lst_items

    @staticmethod
    def get_item_details_in_path(bkt,path):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(name=bkt)
        lst_items = [[x.key,x.size,x.last_modified] for x in bucket.objects.filter(Prefix=path)]
        df_items = pd.DataFrame(lst_items,columns=['key','size','last_modified'])
        return df_items


    @staticmethod
    def save_pickle(bkt,path,obj):
        s3 = boto3.resource('s3')
        sess = boto3.session.Session()
        s3_resource = sess.client('s3')
        pickle_byte_obj = pickle.dumps(obj)
        s3_resource.put_object(Body=pickle_byte_obj, Bucket=bkt,
                               Key=path)

    @staticmethod
    def read_pickle(bkt,path):
        s3 = boto3.resource('s3')
        obj = pickle.loads(
            s3.Bucket(bkt).Object(path).get()['Body'].read())
        return (obj)

    @staticmethod
    def write_text(bkt,path,text):
        s3_resource = boto3.client('s3')
        s3_resource.put_object(Body=text.encode("utf-8"), Bucket=bkt,
                               Key=path)

    @staticmethod
    def read_text(bkt, path):
        s3_client = boto3.client('s3')
        obj = s3_client.get_object(Bucket=bkt, Key=path)
        txt = BytesIO(obj['Body'].read()).getvalue().decode("utf-8")
        return txt



if __name__ == "__main__":
    pass
    # Test
