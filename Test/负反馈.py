def feedback(gin, uin, uout):
    ui = gin - uout/10
    uo = uin*5
    return  [ui,uin,uo,uout]


def main():
    gin_constant = 3
    uin_constant = 3
    uout_constant = 0

main()