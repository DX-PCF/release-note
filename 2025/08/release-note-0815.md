
# Title: August 12, 2025 
Link: https://cloud.google.com/release-notes#August_12_2025<br>
# Cloud Service Mesh
## Announcement
原文: The following images are now rolling out for managed Cloud Service Mesh:
- 1.21.5-asm.55 is rolling out to the rapid release channel.
- 1.20.8-asm.48 is rolling out to the regular release channel.
- 1.19.10-asm.48 is rolling out to the stable release channel.

説明:
Google CloudのマネージドCloud Service Meshにおいて、新しいイメージバージョンが各リリースチャネル（rapid、regular、stable）に順次展開されています。これにより、基盤となるIstioコンポーネントの更新、バグ修正、およびパフォーマンス改善が含まれている可能性があります。

影響有無:
影響は限定的ですが、間接的な影響は考慮する必要があります。
マネージドサービスであるため、お客様側での直接的な操作は不要で、これらのバージョンは各チャネルに沿って自動的に適用されます。通常、これらの更新は後方互換性を維持するように設計されていますが、稀に予期せぬ動作変更が発生する可能性もゼロではありません。

対処方法:
即座に対応が必要な作業はありません。しかし、新しいバージョンが適用された後、ご利用中のサービスにおいて異常がないか、アプリケーションのログやメトリクスを監視することを推奨します。特に、本番環境で運用している場合は、更新後のサービスの健全性を注意深く確認してください。リリースチャネルの選択により更新時期が異なりますので、その点も考慮に入れてください。

用語説明:
*   **Cloud Service Mesh**: Google Cloudが提供するフルマネージドのサービスメッシュソリューションです。オープンソースのIstioをベースにしており、マイクロサービスの接続、監視、セキュリティ保護を簡素化します。
*   **Istio**: サービスメッシュを実装するためのオープンソースプラットフォームです。マイクロサービス間のトラフィック管理、セキュリティ、可観測性を提供します。
*   **リリースチャネル (Release Channel)**: Google Cloudのマネージドサービスにおいて、機能の更新や修正が提供される頻度と安定性のレベルを示す区分です。
    *   **Rapid channel**: 最新の機能や修正が最も早く提供されますが、安定性は保証されにくい傾向があります。開発環境やテスト環境での利用が推奨されます。
    *   **Regular channel**: 最新機能と安定性のバランスが取れています。
    *   **Stable channel**: 最も安定性が重視され、十分にテストされたバージョンが提供されます。本番環境での利用が推奨されます。
*   **ロールアウト (Rolling Out)**: ソフトウェアの新しいバージョンや更新を、ユーザーやシステム全体に段階的に展開していくプロセスを指します。これにより、問題発生時の影響範囲を最小限に抑えることができます。
# Title: August 11, 2025 
Link: https://cloud.google.com/release-notes#August_11_2025<br>
以下にリリースノートに対する調査結果をまとめます。

---

# BigQuery
## Changed
原文: BigQuery data preparations are now represented in the SQLX format and in the pipe query syntax to simplify the CI/CD code review process. For more information, see Manage data preparations.
[Manage data preparations](https://cloud.google.com/bigquery/docs/manage-data-preparations)

説明：
BigQueryのデータ準備機能において、新しくSQLXフォーマットとパイプクエリ構文がサポートされました。これにより、データ準備の定義がより構造化され、CI/CDパイプラインにおけるコードレビューのプロセスが簡素化されることが期待されます。

影響有無：
影響なし。
これは新しい記述形式の導入であり、既存のデータ準備ジョブやクエリの動作に影響を与えるものではありません。既存のワークロードは引き続きこれまで通り動作します。CI/CDパイプラインにおいてこの新しいフォーマットを採用するかどうかは任意です。

対処方法：
特別な対処は不要です。
もし、データ準備の定義とCI/CDでの管理を改善したい場合は、[Manage data preparations](https://cloud.google.com/bigquery/docs/manage-data-preparations) ドキュメントを参照し、新しいSQLXフォーマットやパイプクエリ構文の利用を検討してください。

用語説明：
*   **SQLXフォーマット**: BigQueryにおけるデータ準備（変換やクレンジング）のロジックを定義するための新しいフォーマットです。SQLとXML/JSONのような構造を組み合わせることで、より構造的かつ宣言的にデータ変換ステップを記述できます。
*   **パイプクエリ構文**: データ変換のステップをパイプ（`|`）で連結することで、データの流れを直感的に表現できる構文です。一連のデータ処理タスクを視覚的に把握しやすくなります。
*   **CI/CD**: 継続的インテグレーション（Continuous Integration）と継続的デリバリー（Continuous Delivery）の略称で、ソフトウェア開発プロセスを自動化し、品質とリリース速度を向上させるための手法です。

---

# Cloud Logging
## Libraries
原文: A weekly digest of client library updates from across the Cloud SDK.
[Cloud SDK](https://cloud.google.com/sdk)
## Java
## Changes for google-cloud-logging
[google-cloud-logging](https://github.com/googleapis/java-logging)
[3.23.2](https://github.com/googleapis/java-logging/compare/v3.23.1...v3.23.2)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 (0a21b83)
[0a21b83](https://github.com/googleapis/java-logging/commit/0a21b83377e6e6a2f4cf98149424a47dcd490c1c)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 (#1843) (975d8ae)
[#1843](https://github.com/googleapis/java-logging/issues/1843)
[975d8ae](https://github.com/googleapis/java-logging/commit/975d8aeca38ff2f2f8317df93a661910969c5fc1)

説明：
Java版のCloud Loggingクライアントライブラリ `google-cloud-logging` がバージョン3.23.2にアップデートされました。このアップデートは主に内部的な依存関係の更新（Javaコードジェネレータ `gapic-generator-java` と `sdk-platform-java-config` のバージョンアップ）であり、APIの変更や新機能の追加は含まれていません。

影響有無：
影響なし。
この変更はJavaクライアントライブラリの内部的な依存関係の更新であり、公開されているAPIの動作やインターフェースには影響しません。既存のJavaアプリケーションやGoogle Cloud Composer（Composer 2.7.1, Airflow 2.7.3）の動作には影響ありません。

対処方法：
特別な対処は不要です。
もしアプリケーションで `google-cloud-logging` ライブラリを直接利用している場合、最新の修正や改善を取り込むために、将来的なアップデート時にこのバージョンへの更新を検討できます。

用語説明：
*   **クライアントライブラリ**: プログラミング言語（この場合はJava）でGoogle Cloudサービスとプログラム的にやり取りするためのコードパッケージです。
*   **依存関係 (dependencies)**: あるソフトウェアが正しく動作するために必要とする、他のソフトウェアコンポーネントやライブラリのことです。
*   **gapic-generator-java**: Google API Client Library for Java のコードを自動生成するためのツールです。

---

# Cloud Storage
## Libraries
原文: A weekly digest of client library updates from across the Cloud SDK.
[Cloud SDK](https://cloud.google.com/sdk)
## Java
## Changes for google-cloud-storage
[google-cloud-storage](https://github.com/googleapis/java-storage)
[2.55.0](https://github.com/googleapis/java-storage/compare/v2.54.0...v2.55.0)
- Add new preview Bucket encryption policy configuration (#3204) (7b250dd)
[#3204](https://github.com/googleapis/java-storage/issues/3204)
[7b250dd](https://github.com/googleapis/java-storage/commit/7b250dd53cfa29bbb6a0a4cb4a345aeb2dab5c86)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 (f98b686)
- Enable ALTS bound token (for DirectPath) in the grpc channel provider (#2919) (38d248d)
[f98b686](https://github.com/googleapis/java-storage/commit/f98b686ef940879458acb1e56339adf869400b94)
[#2919](https://github.com/googleapis/java-storage/issues/2919)
[38d248d](https://github.com/googleapis/java-storage/commit/38d248d9511e808e88c1bac0b6bb2ba54897830d)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 (#3213) (86ff697)
[#3213](https://cloud.google.com/sdk)
[86ff697](https://github.com/googleapis/java-storage/commit/86ff69788b30d8f82b6b95d010df507093852889)

説明：
Java版のCloud Storageクライアントライブラリ `google-cloud-storage` がバージョン2.55.0にアップデートされました。主な変更点は以下の通りです。
*   プレビュー版のバケット暗号化ポリシー設定が追加されました。
*   内部的な依存関係（`gapic-generator-java` と `sdk-platform-java-config`）が更新されました。
*   gRPCチャネルプロバイダにおいて、DirectPath用のALTS bound tokenが有効化されました。

影響有無：
影響なし。
このアップデートは、既存のAPIの動作を変更する破壊的変更を含んでいません。
*   新しいバケット暗号化ポリシーはプレビュー機能であり、明示的に利用しない限り影響はありません。
*   ALTS bound tokenの有効化は、DirectPathを使用している環境において、通信のセキュリティやパフォーマンスに影響を与える可能性がありますが、一般的な利用においては透過的であり、既存アプリケーションの動作に影響を与えるものではありません。
*   Google Cloud Composer（Composer 2.7.1, Airflow 2.7.3）のCloud Storage関連のオペレータに直接的な影響はありません。

対処方法：
特別な対処は不要です。
もしアプリケーションで `google-cloud-storage` ライブラリを直接利用しており、新しいプレビュー機能であるバケット暗号化ポリシーの設定をプログラムから行いたい場合は、このバージョンへアップデートすることを検討してください。DirectPath環境を利用している場合は、ALTS bound tokenの恩恵を受けることができます。

用語説明：
*   **バケット暗号化ポリシー**: Cloud Storageバケットに保存されるオブジェクトの暗号化に関する設定を管理するためのポリシーです。新機能は、このポリシーをより柔軟に設定できるものと推測されます。
*   **ALTS (Application Layer Transport Security)**: Googleのインフラストラクチャ内部でサービス間の通信を保護するための認証、認可、暗号化プロトコルです。
*   **DirectPath**: Google Cloudサービスへのネットワークパスを最適化し、低レイテンシと高スループットを実現する機能です。
*   **gRPCチャネルプロバイダ**: gRPC（高性能なオープンソースのRPCフレームワーク）による通信を行うためのネットワーク接続を提供するコンポーネントです。