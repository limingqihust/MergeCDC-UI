
def UpdateConfig(total_node_num, file_distribution, rack_config):
    # print(total_node_num)
    # print(len(file_distribution.splitlines()))
    # assert total_node_num == len(file_distribution.splitlines()) + 2
    # assert total_node_num == len(rack_config.split()) + 2

    with open('./MergeCDC/Distribution/Distribution', 'w') as file:
        file.write(file_distribution)
        file.write('\n')
        file.write(rack_config)

