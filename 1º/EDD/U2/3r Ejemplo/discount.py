def calculate_discount(total, num_items, promo_code=None):
    discount=0

    # verificamos la cantidad de productos
    if num_items>=5:
        discount+=10
    elif num_items==4:
        discount+=5

    # verificamos total
    if total>100:
        discount+=15

    # verificamos codigo promocional
    if promo_code=="DESC20":
        discount+=20
    elif promo_code=="DESC10":
        discount+=10

    if discount>=40:
        discount=40

    final_price=total-(total * discount / 100)
    return final_price, discount


def main():
    purchase1=calculate_discount(120, 3, "DESC20")
    purchase2=calculate_discount(80, 4, "DESC10")
    purchase3=calculate_discount(50, 6)
    purchase4=calculate_discount(150, 5)
    purchase5=calculate_discount(200, 7, "DESC20")

    print(f"Compra 1: Precio final={round(purchase1[0],2)}, Descuento={purchase1[1]}%")
    print(f"Compra 2: Precio final={round(purchase2[0],2)}, Descuento={purchase2[1]}%")
    print(f"Compra 3: Precio final={round(purchase3[0],2)}, Descuento={purchase3[1]}%")
    print(f"Compra 4: Precio final={round(purchase4[0],2)}, Descuento={purchase4[1]}%")
    print(f"Compra 5: Precio final={round(purchase5[0],2)}, Descuento={purchase5[1]}%")


if __name__ == "__main__":
    main()
