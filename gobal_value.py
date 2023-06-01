class g_var(object):
    _global_dic = {}

    def set_dic(self,key,value):
        self._global_dic[key]=value

    def get_dict(self,key):
        return self._global_dic[key]

    def show_dict(self):
        return self._global_dic
