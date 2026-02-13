import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# 1. LOAD DATA
df = pd.read_csv(r'C:\Users\Lenovo\Desktop\Thuan\nmlt\hour.csv')

# ==============================================================================
# BÍ KÍP: THÊM FEATURE QUÁ KHỨ (LAG FEATURES)
# Tạo cột 'prev_cnt': Số lượng xe của 1 giờ trước đó
# ==============================================================================
# Sắp xếp theo thời gian để chắc chắn dòng trên là giờ trước của dòng dưới
df = df.sort_values('instant') 

# Lấy cột cnt dịch xuống 1 dòng (Lag 1)
df['prev_cnt'] = df['cnt'].shift(1)

# Lấy cột cnt dịch xuống 2 dòng (Lag 2 - Tùy chọn, thêm vào càng chính xác)
df['prev_cnt_2'] = df['cnt'].shift(2)

# Xóa các dòng đầu tiên bị NaN do dịch chuyển
df = df.dropna()
# ==============================================================================

# Bỏ các cột không cần thiết (Bỏ luôn 'atemp' vì tương quan cao với 'temp')
drop_cols = ['instant', 'dteday', 'casual', 'registered', 'atemp']
df = df.drop(drop_cols, axis=1)

# Log Transform
X = df.drop('cnt', axis=1)
y = df['cnt'].values
y_log = np.log1p(y)

# One-Hot Encoding
X = pd.get_dummies(X, columns=['season', 'weathersit', 'mnth', 'hr', 'weekday'], drop_first=True)

# Split
X_train, X_test, y_train_log, y_test_log = train_test_split(X, y_log, test_size=0.2, random_state=42)

# 2. TRAIN RANDOM FOREST
print("Đang chạy Random Forest với Lag Features...")
rf_model = RandomForestRegressor(n_estimators=250, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train_log)

# 3. ĐÁNH GIÁ
y_pred_log = rf_model.predict(X_test)

# Đổi ngược log
y_test_origin = np.expm1(y_test_log)
y_pred_origin = np.expm1(y_pred_log)

rmse = np.sqrt(mean_squared_error(y_test_origin, y_pred_origin))
mae = mean_absolute_error(y_test_origin, y_pred_origin)
r2 = r2_score(y_test_origin, y_pred_origin)

print("\n" + "="*40)
print("KẾT QUẢ VỚI LAG FEATURES (QUÁ KHỨ)")
print("="*40)
print(f"RMSE: {rmse:.4f}")
print(f"MAE : {mae:.4f}")
print(f"R2  : {r2:.4f}") 
print("="*40)