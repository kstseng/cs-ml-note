def moveTower(height, fromPole, toPole, withPole):
    """
    """
    if height >= 1:
        ## 把上 n-1 個 disk 從 fromPole 移動到 withPole
        moveTower(height - 1, fromPole, withPole, toPole)
        ## Base case: 當只有一個 disk 時，單純把 disk 從 fromPole 移動到 toPole
        moveDisk(fromPole, toPole)
        ## 把上 n-1 個 disk 從 withPole 移動到 toPole
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fromPole, toPole):
    print("move disk from {} to {}".format(fromPole, toPole))

def main():
    moveTower(3, 'A', 'B', 'C')

if __name__ == "__main__":
    main()
