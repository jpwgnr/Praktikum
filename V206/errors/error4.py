import sympy 
def error(f, err_vars=None):
    from sympy import Symbol, latex 
    s = 0
    latex_names = dict()

    if err_vars == None:
        err_vars = f.free_symbols 

    for v in err_vars: 
        if v != b and v != c and v!= d: #add here all the variables you want as constants. for more than 2 use an "and".  
            err = Symbol('latex_std_'+ v.name)
            s += f.diff(v)**2 * err**2 
            latex_names[err] = '\\sigma_{' + latex(v) + '}'

    return latex(sympy.sqrt(s), symbol_names=latex_names)

a, b, c, d, e, f, g =sympy.var('m_2 c_w m_k c_k L T_2 t') #initalise all your variables at this point

f = (a*b + c*d)/e *f/g  #input your function at this point

file = open("error4.txt", "w")
file.write("Formel: {}\n\nFehlerfortpflanzung: {}".format(f, error(f)))
file.close()