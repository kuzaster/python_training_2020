from task02 import ElderDiscount, MorningDiscount, Order


def test_applying_discount_programs_for_method_final_price():
    morning_discount = MorningDiscount()  # 50% discount
    elder_discount = ElderDiscount()  # 90% discount
    order_1 = Order(100, morning_discount)
    order_2 = Order(100, elder_discount)

    assert order_1.final_price() == 50
    assert order_2.final_price() == 10


def test_changing_applied_discount_program():
    morning_discount = MorningDiscount()  # 50% discount
    elder_discount = ElderDiscount()  # 90% discount

    order_1 = Order(100, morning_discount)  # applied 50% discount
    assert order_1.final_price() == 50

    order_1.discount = elder_discount  # changed discount to 90%
    assert order_1.final_price() == 10
