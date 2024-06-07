# Cú pháp SLQ
- Dùng lệnh select để chọn tất cả các cột (Không phân biệt viết hoa và viết thường)
```sql
SELECT * FROM customer;
```
# Một số lệnh quan trọng trong SQL
- `SELECT`:Chọn tất cả
- `UPDATE`:Cập nhật
- `DELETE`:Xóa dữ liệu
- `INSERT INTO`: Chèn dữ liệu 
- `CREATE DATABASE`: Thêm mới dữ liệu
- `ALTER DATABASE`: Thay đổi dữ liệu
- `CREATE TABLE`: Thêm mới bảng
- `ALTER TABLE`: Thay đổi bảng
- `DROP TABLE`: Xóa bảng
- `CREATE INDEX`: Thêm chỉ mục
- `DROP INDEX`: xóa chỉ mục
# SQL select
- Dùng `SELECT` để chọn dữ liệu trong cơ sở dữ liệu, lấy dữ liệu từ nhiều cột trong bảng mà bạn mong muốn
```sql
SELECT CustomerName, City From Customer;
```
- `SELECT DISTINCT` để chọn dữ liệu sẽ lọc những sự trùng lập 
```sql
SELECT DISTINCT Country from Customer;
```
- `Count Distinct` đếm sự khác biệt, hàm này không hỗ trợ trong CSDL của MS Access
```sql
Select count(Distinct Country) FROM Customer;
```
- Có thể sử dụng cách sau để dùng cho MS Access
```sql
SELECT Count(*) AS DistinctCountries
FROM (SELECT DISTINCT Country FROM Customers);
```
# sql where
