import sympy 
def error(f, err_vars=None):
    from sympy import Symbol, latex 
    s = 0
    latex_names = dict()

    if err_vars == None:
        err_vars = f.free_symbols 

    for v in err_vars: 
        #if v != (a and b): #add here all the variables you want as constants. for more than 2 use an "and".  
            err = Symbol('latex_std_'+ v.name)
            s += f.diff(v)**2 * err**2 
            latex_names[err] = '\\sigma_{' + latex(v) + '}'

    return latex(sympy.sqrt(s), symbol_names=latex_names)

a, b =sympy.var('T_1 T_2') #initalise all your variables at this point

f = a/(a-b) #input your function at this point

file = open("error2.txt", "w")
file.write("Formel: {}\n\nFehlerfortpflanzung: {}".format(f, error(f)))
file.close()