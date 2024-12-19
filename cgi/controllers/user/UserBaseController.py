from controllers.ApiController import ApiController


class UserBaseController(ApiController):

    def __init__(self):
        super().__init__()
        self.response.meta.add('ctr', 'UserBaseController')

    def do_get(self):
        return {'user' : 'works'}