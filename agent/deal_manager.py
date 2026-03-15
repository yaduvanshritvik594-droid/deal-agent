class DealManager:
    def __init__(self):
        # Initialize a deal storage
        self.deals = {}
        self.current_id = 1

    def create_deal(self, title, description, amount):
        deal_id = self.current_id
        self.deals[deal_id] = {
            'title': title,
            'description': description,
            'amount': amount,
            'status': 'active'
        }
        self.current_id += 1
        return deal_id

    def update_deal(self, deal_id, title=None, description=None, amount=None, status=None):
        if deal_id not in self.deals:
            raise ValueError('Deal not found')
        if title:
            self.deals[deal_id]['title'] = title
        if description:
            self.deals[deal_id]['description'] = description
        if amount:
            self.deals[deal_id]['amount'] = amount
        if status:
            self.deals[deal_id]['status'] = status
        return self.deals[deal_id]

    def retrieve_deal(self, deal_id):
        if deal_id not in self.deals:
            raise ValueError('Deal not found')
        return self.deals[deal_id]

    def list_active_deals(self):
        return {deal_id: deal for deal_id, deal in self.deals.items() if deal['status'] == 'active'}

    def deactivate_deal(self, deal_id):
        if deal_id in self.deals:
            self.deals[deal_id]['status'] = 'inactive'
        else:
            raise ValueError('Deal not found')
