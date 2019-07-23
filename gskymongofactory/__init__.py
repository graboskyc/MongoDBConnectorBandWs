import pymongo
from pymongo import WriteConcern

class gskymongofactory:
    _uri = ""
    _conn = ""
    _dblist = []
    _session = None

    def __init__(self, uri):
        self._uri = uri
        try:
            self._conn = pymongo.MongoClient(uri)
            self._dblist = self._conn.database_names()
        # bad un/pw
        except pymongo.errors.OperationFailure as e:
            raise GskyError("Bad Credentials: " + e.details['codeName'],e)
        # can't connect
        except pymongo.errors.ServerSelectionTimeoutError as e:
            raise GskyError("Server Connection Error",e)

    def doAgg(self, db, col, pipeline, appAutoRetry=0):
        try:
            if db in self._dblist:
                return self._conn[db][col].aggregate(pipeline)
            else:
                raise GskyError("Database not found",None)
        except pymongo.errors.OperationFailure as e:
            if(appAutoRetry == 0):
                raise GskyError("App Retry Count Exceeded: " + e.details['errmsg'],e)
            else:
                newRetry = appAutoRetry-1
                self.doAgg(db, col, pipeline, appAutoRetry=newRetry)

    def doFindOne(self, db, col, query, projection=None, appAutoRetry=0):
        try:
            if db in self._dblist:
                return self._conn[db][col].find_one(query, projection)
            else:
                raise GskyError("Database not found",None)

        except pymongo.errors.OperationFailure as e:
            if(appAutoRetry == 0):
                raise GskyError("App Retry Count Exceeded: " + e.details['errmsg'],e)
            else:
                newRetry = appAutoRetry-1
                self.doFindOne(db, col, query, projection=projection, appAutoRetry=newRetry)
    
    def doInsertOne(self, db, col, document, bypassValidation=False, appAutoRetry=0):
        try:
            if db in self._dblist:
                return self._conn[db][col].insert_one(document, bypass_document_validation=bypassValidation)
            else:
                raise GskyError("Database not found",None)
        except pymongo.errors.OperationFailure as e:
            if("not authorized" in e.details['errmsg']):
                raise GskyError("Permissions Error: " + e.details['errmsg'],e)
            elif(appAutoRetry == 0):
                raise GskyError("App Retry Count Exceeded: " + e.details['errmsg'],e)
            else:
                newRetry = appAutoRetry-1
                self.doInsertOne(db, col, document, bypass_document_validation=bypassValidation, appAutoRetry=newRetry)

class GskyError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors