from mite.datapools import RecyclableIterableDataPool

user_ids = RecyclableIterableDataPool([(i,) for i in range(5000)])
