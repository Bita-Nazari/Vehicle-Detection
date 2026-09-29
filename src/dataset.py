from torchvision import datasets,transforms
from sklearn.model_selection import train_test_split
from torch.utils.data import Subset
from pathlib import Path
from torch.utils.data import DataLoader


train_path = Path("data/train")
test_path = Path("data/test")


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
    
])


train_data = datasets.ImageFolder(train_path,transform=transform)
test_data = datasets.ImageFolder(test_path,transform=transform)

train_indices, val_indices = train_test_split(
    range(len(train_data)),
    test_size=0.2,
    random_state=42,
    stratify=train_data.targets
)

train_dataset = Subset(train_data , train_indices)
val_dataset = Subset(train_data , val_indices)
test_dataset = test_data

train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=32,
    shuffle=False
)

test_loader = DataLoader(
    test_dataset,
    batch_size=32,
    shuffle=False
)

images,labels = next(iter(train_loader))

print(images.shape)
print(labels.shape)
print(labels[:10])