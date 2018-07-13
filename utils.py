def print_regr(desc_y, regr):
    lista = [f'{value:.3f} x {key}' for key, value in regr.params.items()]
    lista[0] = f"{regr.params['Intercept']:.3f}"
    print(desc_y + ' = ' + ' + '.join(lista))
    lista = [f'({value:.3f})' for key, value in regr.bse.items()]
    lista[0] = f"({regr.bse['Intercept']:.3f})"
    print('\t'.join(lista))
    print(f'n = {regr.nobs}, R^2 = {regr.rsquared:.4f}')