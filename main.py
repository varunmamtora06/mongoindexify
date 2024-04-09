from pymongo import MongoClient, IndexModel
import argparse

class MyClient:
    def __init__(self, conn_str, db_name, coll_name):
        self.mongodb_client = MongoClient(conn_str)
        self.db = self.mongodb_client[db_name]
        self.collection = self.db[coll_name]

    def print_indexes(self):
        print(f"indexes: {[x for x in self.collection.list_indexes()]}")

    def export_indexes(self):
        indexes_cursor = self.collection.list_indexes()
        index_models = []
        for index in indexes_cursor:
            if index["name"] != "_id_": # ignore _id_ index cuz its there already
                if 'weights' in index:
                    index_model = IndexModel(index["key"], name=index["name"], weights=index["weights"])
                else:
                    index_model = IndexModel(index["key"], name=index["name"], unique=index.get("unique", False))
                index_models.append(index_model)
        return index_models

    def apply_indexes(self, index_models):
        self.collection.create_indexes(index_models)

def main(args):
    src_mongodb_client, dest_mongodb_client = [MyClient(args.src, args.srcdb, args.srccoll),
                                               MyClient(args.dest, args.destdb, args.destcoll)]

    source_index_models = src_mongodb_client.export_indexes()
    dest_mongodb_client.apply_indexes(source_index_models)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import indexes")
    parser.add_argument("-src", "--src", help = "Source string")
    parser.add_argument("-srcdb", "--srcdb", help = "Source db")
    parser.add_argument("-srccoll", "--srccoll", help = "Source collection")
    
    parser.add_argument("-dest", "--dest", help = "Destination string")
    parser.add_argument("-destdb", "--destdb", help = "Destination db")
    parser.add_argument("-destcoll", "--destcoll", help = "Destination collection")
    args = parser.parse_args()

    # TEST
    # args.src="mongodb://localhost:27017"
    # args.srcdb="test"
    # args.srccoll="test2"

    # args.dest="mongodb://localhost:27017"
    # args.destdb="test"
    # args.destcoll="testcoll"
    
    main(args)