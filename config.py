from enum import Enum

class ConfigStatus(Enum):
    Success = 1
    FileDistributionError = 2
    NodeDistributionError = 3
    Default = 4



def CheckConfig(total_node_num, file_distribution, rack_config):
    if file_distribution == '' or rack_config == '':
        return ConfigStatus.Default
    if total_node_num != len(file_distribution.splitlines()) + 2:
        return ConfigStatus.FileDistributionError
    if total_node_num != len(rack_config.split()) + 2:
        return ConfigStatus.NodeDistributionError
    return ConfigStatus.Success



def UpdateConfig(total_node_num, file_distribution, rack_config):
    with open('./MergeCDC/Distribution/Distribution', 'w') as file:
        file.write(file_distribution)
        file.write('\n')
        file.write(rack_config)

def ParseData(result):
    data = []
    for line in result.splitlines():
        words = line.split()
        data.append((words[0], words[1], words[2]))
    return data
            

