day_num = 6

file_load = open("input6.txt", "r")
file_in = file_load.read()
file_load.close() 
file_in = file_in.split("\n\n")

def run():

    def yes(input_in):
        group_ans = [set(temp_group.replace("\n","")) for temp_group in input_in]
        total_ans = 0
        for temp_group in group_ans:
            total_ans += len(temp_group)
        return total_ans

    def only(input_in):
        group_ans = [temp_group.split("\n") for temp_group in input_in]
        group_final = []
        for temp_group in group_ans:
            group_new = []
            for temp_person in temp_group:
                group_new.append(set(list(temp_person)))
            group_final.append(group_new[0].intersection(*group_new))
        total_ans = 0
        for temp_group in group_final:
            total_ans += len(temp_group)
        return total_ans

    return yes(file_in), only(file_in)