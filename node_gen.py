nodes = []
links = []

def node_gen(input):
    """Generator that yields nodes"""
    try: 
        i = 1
        for num in input:
            try:
                num = int(num)
                node = ("node_%s" % i)
                node = node.replace(" ", "")
                link = ("%s.next" % node)
                link = link.replace(" ", "")   
                next_node = ("node_%s" % (i+1))
                next_node = next_node.replace(" ", "")
                if i == 1:
                    nodes.append(f"{node} = Node('{num}')")
                elif i > 1:
                    prev_node = ("node_%s" % (i-1))
                    prev_node = prev_node.replace(" ", "")
                    nodes.append(f"{node} = Node('{num}', prev={prev_node})")
                links.append(f"{link} = {next_node}")
                i += 1
            except:
                pass
        del links[-1]
    except:
        print("Error: Please enter a valid input containing numbers")
        quit()
    print(f'\n{nodes}\n\n{links}')
    return True     

node_gen((1, 7, 4, 2, 9, 8, 10, -4, 0, 3))    