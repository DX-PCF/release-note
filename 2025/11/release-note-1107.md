
# Title: November 05, 2025 
Link: https://docs.cloud.google.com/release-notes#November_05_2025<br>
# Cloud Composer

## Announcement

原文: We strongly recommend to use highly resilient environments for production use cases. Highly resilient environments provide high availability and use built-in redundancy and failover mechanisms to reduce the environment's susceptibility to zonal failures and single point of failure outages.
[highly resilient environments](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments)

説明:
Google Cloud Composerにおいて、プロダクション用途の環境では「Highly Resilient Environments（高い回復力を持つ環境）」を使用することを強く推奨しています。これらの環境は、高可用性を提供し、ゾーン障害や単一障害点（SPOF）による停止に対する脆弱性を低減するために、組み込みの冗長性およびフェイルオーバーメカニズムを利用しています。この推奨は、特にComposer 3における新しい高可用性構成を指しています。

影響有無:
**直接的な影響はありません。**
このアナウンスは、既存のComposer 2.7.1環境に対する変更を伴うものではなく、将来的なベストプラクティスの推奨事項です。現在ご利用中のComposer 2環境は、この機能の対象外（Composer 3で導入された機能）であるため、既存のサービス稼働には影響しません。しかし、プロダクション環境の可用性向上を検討する場合、将来的なComposer 3へのアップグレードと、Highly Resilient Environmentsの導入が推奨される選択肢となります。

対処方法:
**即座の対処は不要です。**
*   **現状維持:** Composer 2.7.1環境は引き続き問題なく動作します。
*   **将来的な検討:** プロダクション環境の可用性をさらに向上させたい場合は、Composer 3へのアップグレードとHighly Resilient Environmentsの構成を検討してください。アップグレードの際には、公式ドキュメントを参照し、既存のワークロードへの影響を評価した上で計画的に実施する必要があります。

用語説明:
*   **Highly Resilient Environments (高い回復力を持つ環境):** Google Cloud Composer 3で導入された高可用性構成の一つで、マルチゾーンにまたがることで、単一ゾーンの障害からサービスを保護し、高い稼働率を維持することを目的としています。コントローラ、スケジューラ、ワーカーなどのコンポーネントが複数のゾーンに分散配置されます。
*   **High Availability (高可用性):** システムが継続して機能し、ユーザーからの要求に応答できる状態を維持する能力。障害が発生してもサービスが停止しない、または短時間で回復することを指します。
*   **Redundancy (冗長性):** システムの一部に障害が発生した場合でも、全体の機能が継続できるように、同じ機能を持つコンポーネントやシステムを複数用意しておくこと。
*   **Failover mechanisms (フェイルオーバーメカニズム):** システムの一部に障害が発生した際に、自動的にもう一方の正常なコンポーネントやシステムに処理を引き継ぐ（切り替える）仕組み。
*   **Zonal failures (ゾーン障害):** Google Cloudの特定のゾーン（地理的に独立したデータセンターのグループ）全体に影響を及ぼす障害。
*   **Single Point of Failure (SPOF) (単一障害点):** システム内で、そのコンポーネントが停止するとシステム全体が機能しなくなるような箇所。SPOFを排除することで、システムの可用性が向上します。
# Title: November 03, 2025 
Link: https://docs.cloud.google.com/release-notes#November_03_2025<br>
ご担当者様

Google Cloudのリリースノートに関する調査結果をご報告いたします。

---

# Pub/Sub
## Changed

原文:
A weekly digest of client library updates from across the Cloud SDK.
## Python
## Changes for google-cloud-pubsub
[google-cloud-pubsub](https://github.com/googleapis/python-pubsub)
[2.32.0](https://github.com/googleapis/python-pubsub/compare/v2.31.1...v2.32.0)
- Adds Python 3.14 support (#1512) (95a2690)
- Debug logs (#1460) (b5d4a45)
- Support the protocol version in StreamingPullRequest (#1455) (e6294a1)
- Ignore future warnings on python versions (#1546) (8e28dea)

説明:
Google Cloud Pub/Sub Python クライアントライブラリ `google-cloud-pubsub` のバージョン `2.32.0` における変更点です。
主な変更点は以下の通りです。
*   **Python 3.14 サポートの追加**: 将来リリースされるPython 3.14バージョンへの対応が追加されました。
*   **デバッグログの改善**: ライブラリ内部のデバッグログに関する改善が行われました。
*   **StreamingPullRequestのプロトコルバージョンサポート**: Pub/Subのストリーミングプル（`StreamingPullRequest`）において、内部的なプロトコルバージョンをサポートするようになりました。これにより、通信の堅牢性や将来的な互換性が向上します。
*   **FutureWarningの抑制**: Pythonの将来のバージョンで発生する可能性のある`FutureWarning`が無視されるようになりました。これは、ライブラリの安定性を高めるための変更です。

影響有無:
**影響なし**

理由:
これらの変更は、Pythonの将来バージョンへの対応、デバッグログの改善、および内部的なプロトコルサポートの追加といった非破壊的なアップデートであり、既存のAPIの振る舞いを変更するものではありません。現在運用中のGoogle Cloud Composer 2 (Compoer version 2.7.1、Airflow version 2.7.3) 環境で使用されている`google-cloud-pubsub`ライブラリのバージョンがこのバージョンより古い場合でも、既存のAirflow DAGsやPythonコードの動作に直接的な影響を与える変更は含まれていません。Python 3.14へのサポート追加は、将来的なPythonバージョンアップグレード時の選択肢を広げるものです。

対処方法:
**不要**

特別な対処は必要ありません。Google Cloud Composer はマネージドサービスであり、基盤となるライブラリのバージョンはComposerのバージョンアップグレードやAirflowのイメージ更新に伴って自動的に更新される可能性があります。もし将来的に`google-cloud-pubsub`ライブラリがこのバージョンに更新されたとしても、既存のワークロードに悪影響を及ぼす変更は含まれていないため、追加の対応は不要です。

用語説明:
*   **google-cloud-pubsub**: Google Cloud Pub/SubサービスとPythonアプリケーション間でメッセージの送受信を行うために使用される公式のPythonクライアントライブラリです。
*   **Python 3.14**: プログラミング言語Pythonのメジャーバージョンの一つで、本リリース時点ではまだ開発中の将来のバージョンです。
*   **StreamingPullRequest**: Google Cloud Pub/Subにおいて、サブスクライバーがPub/Subサービスからメッセージを継続的にストリーミング形式で取得（プル）するためのRPCメソッドです。長期接続を維持し、低レイテンシでメッセージを受信する場合に利用されます。
*   **FutureWarning**: Pythonで、現在のコードが将来のPythonバージョンで非推奨になる、あるいは動作が変更される可能性がある場合に発行される警告カテゴリです。この警告を無視することで、ライブラリの利用者が将来のPythonバージョンアップグレード時に不必要な警告に煩わされるのを防ぎます。