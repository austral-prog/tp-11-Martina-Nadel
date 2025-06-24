def read_file_to_dict(filename):
    sales_dict = {}
    with open(filename, 'r') as file:
        line = file.readline().strip()
        sales = line.split(';')
        for sale in sales:
            if sale:
                try:
                    product, value = sale.split(':')
                    value = float(value)
                    if product in sales_dict:
                        sales_dict[product].append(value)
                    else:
                        sales_dict[product] = [value]
                except ValueError:
                    print(f"Error al procesar la venta: '{sale}'. Revisa el formato.")
    return sales_dict


def process_dict(data):
    for product, values in data.items():
        total = sum(values)
        average = total / len(values)
        print(f"{product}: ventas totales ${total:.2f}, promedio ${average:.2f}")
    pass

