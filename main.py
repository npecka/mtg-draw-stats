from random import randint

def create_deck():
    deck_list = []
    with open("deck.txt") as myfile:
        for line in myfile:
            var, name = line.partition(" ")[::2]
            if int(var) > 1:
                for i in range(int(var)):
                    deck_list.append((name.strip(), 1))
            else:
                deck_list.append((name.strip(), var))
    return deck_list


def create_hand(hand, deck_list):
    deck_list_copy = deck_list.copy()
    k = 59
    for i in range(7):
        j = randint(0, k)
        hand.append(deck_list_copy[j])
        deck_list_copy.remove(deck_list_copy[j])
        k -= 1


def create_hand_multiple(multi_hand, num):
    total = num * 7
    hand = []
    deck_list = create_deck()
    create_hand(hand, deck_list)
    hand_first = []
    for a_tuple in hand:
        hand_first.append(a_tuple[0])
    for i in range(len(hand_first)):
        if hand_first[i] in deck_stats:
            lst = list(multi_hand.get(hand_first[i]))
            lst[0] = lst[0] + 1
            lst[1] = "{:.2%}".format((lst[0] / total))
            t = tuple(lst)
            multi_hand[hand_first[i]] = t

        else:
            multi_hand[hand_first[i]] = 1, "{:.2%}".format((1/total))
    return multi_hand


if __name__ == '__main__':
    deck_stats = {}
    iterations = 1000;
    for i in range(iterations):
        deck_stats = create_hand_multiple(deck_stats, iterations)

    print(len(deck_stats))

    for key, value in deck_stats.items():
        print(key, ' : ', value)
