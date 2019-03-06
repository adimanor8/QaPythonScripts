import yaml
def yaml_dump(filepath):
        data = {"ser": {"a1": 3, "a2": 2},"db":2}
        yaml.dump(data,open(filepath,"w"),default_flow_style=False)
def yaml_loader(filepath):
    with open(filepath,"r") as file_descriptor:
        data=yaml.load(file_descriptor)
        return data



if __name__ == '__main__':
    filepath="test.yaml"
    data=yaml_dump(filepath)
    data2=yaml_loader(filepath)
    print(data2)

