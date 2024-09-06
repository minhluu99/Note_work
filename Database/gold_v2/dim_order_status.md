
| STATUS                   | Trạng Thái Đơn Hàng    |       SO       | Trạng thái SO      | DO                |
| ------------------------ | ---------------------- | -------------- | ------------------ | ----------------- |
| RESERVING                | Đã Xác nhận            | SOBD35072304   | Đang Giữ hàng      | -                 |
| WAIT_TO_PICK             | Đang Xử lý             | SOBD35103527   | Đang Lấy Hàng      | -                 |
| WAIT_TO_PICK             | Đang Xử lý             | SOBD35060880   | Đang Lấy Hàng      | -                 |
| PICKING                  |                        |                |                    |                   |
| WAIT_TO_CHECK            |                        |                |                    |                   |
| CHECKING                 |                        |                |                    |                   |
| WAIT_TO_PACK             |                        |                |                    |                   |
| PACKING                  |                        |                |                    |                   |
| WAIT_TO_DELIVERY         | Chờ Giao Hàng          | SOHN35102128   | Chờ Vận Chuyển     | Chờ Vận Chuyển    |
| DELIVERING               |                        |                |                    |                   |
| DELIVERED                |                        |                |                    |                   |
| CANCEL                   |                        |                |                    |                   |
| COMPLETED                | Đã Hoàn Tất            | SOBD35099296   | Hoàn Thành         | Hoàn Thành        |
| RETURN                   |                        |                |                    |                   |
| RETURNING                | Đang Vận chuyển        | SOBD35083895   | Đang Trả Hàng      | Đang Giao Hàng    |
| RETURNED                 |                        |                |                    |                   |
| LOST                     | Đã Hủy                 | SOHN34429319   | Thất Lạc/Mất Hàng  | Không Xác Định    |
| LOST                     | Đã Hủy                 | SOHN34841719   | Thất Lạc/Mất Hàng  | Thất Lạc/Mất Hàng |
|                          |                        |                |                    |                   |
| LOST                     | Đã Hủy                 | SOHN34436485   | Thất Lạc/Mất Hàng  | Đang Giao Hàng    |
|            DRAFT         | -- Quá cũ              |                |                    |                   |
| WAIT_TO_LIQUIDATION      |                        |                |                    |                   |
| LIQUIDATED               |                        |                |                    |                   |



| Status |       So       | Trạng thái So     |    DO           | Trạng thái DO     |
| ------ | -------------- | ----------------- | --------------- | ----------------- |
| LOST   | SOHN34841719   | Thất Lạc/Mất Hàng | SOHN34841719-F  | Thất Lạc/Mất Hàng |
|        |                |                   |                 |                   |
CANCEL  | SOHN35058785  | Đã Hủy            | SOHN35058785-F | Chờ Vận Chuyển
DRAFT    | SOBD35093736  | Chờ Vận Chuyển    | SOBD35093736-F | Chờ Vận Chuyển
DRAFT               | SOHN35094608  | Chờ đóng gói      |
WAIT_TO_DELIVERY    | SOBD35084912  | Chờ Vận Chuyển    | SOBD35084912-F | Chờ Vận Chuyển
DELIVERING          | SOBD35085000  | Đang Giao Hàng    | SOBD35085000-F | Đang Giao Hàng
DELIVERED           | SOHN35049558  | Đã Giao Hàng      | SOHN35049558-F | Đã Giao Hàng
RETURN              | SOBD35083895  | Đang Trả Hàng     | SOBD35083895-F | Đang Giao Hàng
RETURN              | SOBD35083895  | Trả Hàng          | SOBD35083895-F | Đang Giao Hàng
RETURNING           | SODN35087384  | Đang Trả Hàng     | SODN35087384-F | Đang Giao Hàng
RETURNING           | SOBD35058226  | Đã Trả Hàng       | SODN35087384-F | Đang Giao Hàng
RETURNED            | SOBD35094345  | Đã Trả Hàng       | SOBD35094345-F | Đang Giao Hàng
RETURNED            | SOBD35094345  | Đã Trả Hàng       | SOBD35094345-F | Đã Trả Hàng
MERGED              | SOBD34057731  | Hoàn Thành        | SOBD34057731-F | Hoàn Thành
COMPLETED           | SOBD35098357  | Hoàn Thành        | SOBD35098357-F | Hoàn Thành
LIQUIDATED          |
WAIT_TO_LIQUIDATION |