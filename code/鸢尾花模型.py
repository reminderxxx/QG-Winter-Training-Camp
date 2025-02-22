import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

# 1. 加载数据集
iris = load_iris()
X = iris.data  # 特征
y = iris.target  # 标签

# 2. 数据划分：训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 将数据保存为 npz 格式
np.savez('iris_data.npz', X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

# 4. 选择分类模型并进行训练
models = {
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'Logistic Regression': LogisticRegression(max_iter=200)
}

# 5. 训练并评估模型
for model_name, model in models.items():
    model.fit(X_train, y_train)  # 训练
    y_pred = model.predict(X_test)  # 预测
    accuracy = accuracy_score(y_test, y_pred)  # 计算准确率
    print(f'{model_name} Accuracy: {accuracy * 100:.2f}%')

    # 若准确率大于90%，可以选择此模型作为最终模型
    if accuracy >= 0.90:
        print(f'{model_name} 达到要求的准确率：{accuracy * 100:.2f}%')
        best_model = model
        break

# 6. 输出最终选择的最佳模型
if best_model:
    print(f'最终选择的模型是：{best_model}')
else:
    print("没有达到 90% 准确率的模型。")
