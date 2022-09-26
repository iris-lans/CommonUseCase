class Model:
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15}
    }


class View:
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')

    def list_pricing(self, services):
        for svc,value in services.items():
            print("For", value['number'],
                  svc, 'message you pay $',
                  value['price'])


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        return (self.view.list_services(self.model.services))

    def get_pricing(self):
        return (self.view.list_pricing(self.model.services))


if __name__ == '__main__':
    controller = Controller()
    print("Services Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()

# => Services Provided:
# => email
# => sms
# => voice
# => Pricing for Services:
# => For 1000 email message you pay $ 2
# => For 1000 sms message you pay $ 10
# => For 1000 voice message you pay $ 15