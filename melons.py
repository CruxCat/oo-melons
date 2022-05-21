"""Classes for melon orders."""
# Create an AbstractMelonOrder class to serve as a base class and refactor.
class AbstractMelonOrder:

    def __init__(self,species,qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
       """Initialize melon order attributes."""
       super().__init__(species,qty)
       self.country_code = country_code
        


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order"""
    order_type = "government"
    tax = 0.00

    def __init__(self, species, qty, passed_inspection=False):
        super().__init__(species, qty)
        #self.passed_inspection = False

    #def mark_inspection(self, passed):
        #self.passed_inspection = passed

    def mark_inspection(self, passed_inspection):
        self.passed_inspection = True
