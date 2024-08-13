c
#set帮助读取，Loader帮助批量方式加载

class ImdbDataset(Dataset):
    def __init__(self) -> None:
        super().__init__()

    def __getitem__(self, index) -> Any:
        return super().__getitem__(index)
    def __len__(self):
        pass