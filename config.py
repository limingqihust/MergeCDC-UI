
def UpdateConfig(total_node_num, file_distribution, rack_config):
    if total_node_num != len(file_distribution.splitlines()) + 1:
        print(f"total_node_num: {total_node_num}, file_distribution: {file_distribution}")
        exit(-1)
    if total_node_num != len(rack_config.split()) + 2:
        print(f"total_node_num: {total_node_num}, rack_config: {rack_config}")
        exit(-1)

    with open('./MergeCDC/Distribution/Distribution', 'w') as file:
        file.write(file_distribution)
    with open('./MergeCDC/Distribution/combination_my', 'w') as file:
        file.write(rack_config)

