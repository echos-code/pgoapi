Native Types
============

+----------+-----------------------------+--------+------------+-------------+
| .proto   |  Notes                      | C++    | Java Type  | Python Type |
| Type     |                             | Type   |            |             |
+==========+=============================+========+============+=============+
| double   |                             | double | double     | float       |
+----------+-----------------------------+--------+------------+-------------+
| float    |                             | float  | float      | float       |
+----------+-----------------------------+--------+------------+-------------+
| int32    | Uses variable-length        | int32  | int        | int         |
|          | encoding. Inefficient for   |        |            |             |
|          | encoding negative numbers – |        |            |             |
|          | if your field is likely to  |        |            |             |
|          | have negative values, use   |        |            |             |
|          | sint32 instead.             |        |            |             |
+----------+-----------------------------+--------+------------+-------------+
| int64    | Uses variable-length        | int64  | long       | int/long    |
|          | encoding. Inefficient for   |        |            |             |
|          | encoding negative numbers – |        |            |             |
|          | if your field is likely to  |        |            |             |
|          | have negative values, use   |        |            |             |
|          | sint64 instead.             |        |            |             |
+----------+-----------------------------+--------+------------+-------------+
| uint32   | Uses variable-length        | uint32 | int        | int/long    |
|          | encoding.                   |        |            |             |
+----------+-----------------------------+--------+------------+-------------+
| uint64   | Uses variable-length        | uint64 | long       | int/long    |
|          | encoding.                   |        |            |             |
+----------+-----------------------------+--------+------------+-------------+
| sint32   | Uses variable-length        | int32  | int        | int         |
|          | encoding. Signed int value. |        |            |             |
|          | These more efficiently      |        |            |             |
|          | encode negative numbers     |        |            |             |
|          | than regular int32s.        |        |            |             |
+----------+-----------------------------+--------+------------+-------------+
| sint64   | Uses variable-length        | int64  | long       | int/long    |
|          | encoding. Signed int value. |        |            |             |
|          | These more efficiently      |        |            |             |
|          | encode negative numbers     |        |            |             |
|          | than regular int64s.        |        |            |             |
+----------+-----------------------------+--------+------------+-------------+
| fixed32  | Always four bytes. More     | uint32 | int        | int         |
|          | efficient than uint32 if    |        |            |             |
|          | values are often greater    |        |            |             |
|          | than 2^28.                  |        |            |             |
+----------+-----------------------------+--------+------------+-------------+
| fixed64  | Always eight bytes. More    | uint64 | long       | int/long    |
|          | efficient than uint64 if    |        |            |             |
|          | values are often greater    |        |            |             |
|          | than 2^56.                  |        |            |             |
+----------+-----------------------------+--------+------------+-------------+
| sfixed32 | Always four bytes.          | int32  | int        | int         |
+----------+-----------------------------+--------+------------+-------------+
| sfixed64 | Always eight bytes.         | int64  | long       | int/long    |
+----------+-----------------------------+--------+------------+-------------+
| bool     |                             | bool   | boolean    | boolean     |
+----------+-----------------------------+--------+------------+-------------+
| string   | A string must always        | string | String     | str/unicode |
|          | contain UTF-8 encoded or    |        |            |             |
|          | 7-bit ASCII text.           |        |            |             |
+----------+-----------------------------+--------+------------+-------------+
| bytes    | May contain any arbitrary   | string | ByteString | str         |
|          | sequence of bytes.          |        |            |             |
+----------+-----------------------------+--------+------------+-------------+
