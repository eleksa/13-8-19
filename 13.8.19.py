count_tickets = int(input('Сколько билетов вы хотите приобрести?\n'))
discount = 0.1
total_summ = 0
for i in range(1, count_tickets + 1):
    age_guest = int(input(f'Укажите возраст {i} гостя: '))
    if age_guest < 18:
        cost_ticket = 0
    elif 18 <= age_guest <= 25:
        cost_ticket = 990
    else:
        cost_ticket = 1390
    total_summ += cost_ticket
if count_tickets > 3:
    discount_summ = total_summ - total_summ * discount
else:
    discount_summ = total_summ
print('Итого к оплате со скидкой', round(discount_summ), 'р.')