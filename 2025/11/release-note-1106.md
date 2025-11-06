
# Title: November 05, 2025 
Link: https://docs.cloud.google.com/release-notes#November_05_2025<br>
# Cloud Composer
## Announcement
原文: We strongly recommend to use highly resilient environments for production use cases. Highly resilient environments provide high availability and use built-in redundancy and failover mechanisms to reduce the environment's susceptibility to zonal failures and single point of failure outages.
[highly resilient environments](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments)

説明:
Google Cloud Composerの本番環境において、「高可用性環境（Highly Resilient Environments）」の利用が強く推奨されるというアナウンスです。高可用性環境は、ゾーン障害や単一障害点（SPOF）によるサービス停止のリスクを低減するため、組み込みの冗長性とフェイルオーバーメカニズムを提供します。提供されているドキュメントリンクはCloud Composer 3の「高可用性環境の設定」に関するものであり、Composer 3で導入されたマルチゾーン配置の機能が主眼となっています。

影響有無:
**影響あり**

理由:
現在ご利用のCloud Composer環境が本番環境であり、かつ高可用性設計が十分に考慮されていない場合、この推奨事項に準拠していないことになります。このアナウンスは既存のサービスの動作を直接変更するものではありませんが、本番稼働しているサービスに対して、可用性に関する潜在的なリスクが存在することを示唆しています。特に、ご利用のComposerがComposer 2（2.7.1）である場合、Composer 3で提供されるネイティブなマルチゾーン高可用性機能は利用できません。そのため、本番環境の可用性要件を満たしているか再評価が必要となります。

対処方法:
1.  **現状の評価**: 現在のCloud Composer環境が、本番環境の可用性要件とこの「高可用性環境」の推奨事項にどれだけ準拠しているかを確認してください。特に、単一ゾーン配置であるか、ゾーン障害発生時の影響範囲がどこまでかなどを確認します。
2.  **Composer 3への移行検討**: アナウンスのリンク先がComposer 3のドキュメントであることからも、GoogleはComposer 3の「高可用性環境」機能の利用を強く推奨していると解釈できます。Composer 3では、コントロールプレーンをマルチゾーンに配置することで、より高い可用性を実現できます。既存のComposer 2環境をComposer 3へアップグレードまたは移行することを検討してください。
3.  **Composer 2での対応**: Composer 3への移行が直ちに困難な場合は、Composer 2環境において、ゾーン障害への耐性を高めるための追加対策を検討してください。例えば、以下の対策が考えられます。
    *   Cloud BuildやTerraformなどを利用した、迅速な環境再構築手順の整備。
    *   Airflow DAGの冪等性（何度実行しても同じ結果になる性質）を確保し、障害発生後の再実行を容易にする。
    *   Airflowワーカーのオートスケーリング設定の最適化。
    *   Airflowメタデータデータベースの定期的なバックアップとリストア手順の確立。
    *   外部依存サービス（データベース、ストレージなど）の高可用性設定を確認し、Composer環境からそれらへの接続に冗長性を持たせる。

用語説明:
*   **Highly Resilient Environments（高可用性環境）**: システムが障害発生時にもサービスを提供し続けられるように設計された環境。単一障害点を排除し、冗長化やフェイルオーバーの仕組みを組み込むことで、サービスの中断時間を最小限に抑えます。Cloud Composer 3においては、コントロールプレーン（Airflowスケジューラ、ウェブサーバー、メタデータデータベースなど）を複数のGoogle Cloudゾーンに分散配置することで実現されます。
*   **Zonal Failures（ゾーン障害）**: Google Cloudの特定のゾーン（データセンター）全体が、停電、ネットワーク障害、自然災害などにより利用不能になること。
*   **Single Point of Failure (SPOF)（単一障害点）**: システム内で、そのコンポーネントが故障するとシステム全体が停止してしまうような箇所。高可用性設計では、SPOFを排除することが重要です。
# Title: November 03, 2025 
Link: https://docs.cloud.google.com/release-notes#November_03_2025<br>
# Pub/Sub
## Changed

原文:
A weekly digest of client library updates from across the Cloud SDK.
[Cloud SDK](https://cloud.google.com/sdk)

## Python
## Changes for google-cloud-pubsub
[google-cloud-pubsub](https://github.com/googleapis/python-pubsub)
[2.32.0](https://github.com/googleapis/python-pubsub/compare/v2.31.1...v2.32.0)
- Adds Python 3.14 support (#1512) (95a2690)
- Debug logs (#1460) (b5d4a45)
- Support the protocol version in StreamingPullRequest (#1455) (e6294a1)

[#1512](https://github.com/googleapis/python-pubsub/issues/1512)
[95a2690](https://github.com/googleapis/python-pubsub/commit/95a26907efecfa5d56b140b7f833640b7fbb21d7)
[#1460](https://github.com/googleapis/python-pubsub/issues/1460)
[b5d4a45](https://github.com/googleapis/python-pubsub/commit/b5d4a458ca9319bebbe3142a1f05d4d4471c8d4d)
[#1455](https://github.com/googleapis/python-pubsub/issues/1455)
[e6294a1](https://github.com/googleapis/python-pubsub/commit/e6294a1883abf9809cb56d5cd4ad25cc501bc994)
- Ignore future warnings on python versions (#1546) (8e28dea)

[#1546](https://github.com/googleapis/python-pubsub/issues/1546)
[8e28dea](https://github.com/googleapis/python-pubsub/commit/8e28dea5b68fc940266d0b1a9f2a07a7b5f10b34)

説明：
このリリースノートは、Cloud SDKに含まれるPub/SubのPythonクライアントライブラリ `google-cloud-pubsub` のバージョン2.32.0における変更点を示しています。主な変更点は以下の通りです。

1.  **Python 3.14のサポート追加**: 新しいPythonバージョンである3.14に対する互換性が追加されました。
2.  **デバッグログの改善**: ライブラリの内部動作に関するデバッグログが強化されました。
3.  **`StreamingPullRequest`におけるプロトコルバージョンサポート**: Pub/Subのストリーミングプル機能で、内部的なプロトコルバージョンをサポートする機能が追加されました。
4.  **将来のPythonバージョンにおける警告の無視**: 将来のPythonバージョンで発生しうる警告を適切に処理し、無視するようになりました。

影響有無：影響なし

理由：
これらの変更は、`google-cloud-pubsub` Pythonクライアントライブラリの機能追加、内部改善、および将来のPythonバージョンへの対応であり、既存のPub/SubサービスAPIや既存のクライアントコードの動作に破壊的な変更（Breaking Change）をもたらすものではありません。

現在利用中のGoogle Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) 環境において、Airflow DAGs内で`google-cloud-pubsub`ライブラリを使用している場合でも、これらの変更は基本的に既存のワークロードに影響を与えません。Python 3.14のサポートは、Composer 2.7.1がPython 3.10をベースとしているため、現時点では直接的な影響はありませんが、将来的なPythonバージョンのサポートを見据えたものです。デバッグログの改善やプロトコルサポートの追加は内部的な改善であり、既存のアプリケーションが明示的にこれらの機能に依存していなければ透過的に機能します。

対処方法：
基本的に対処は不要です。
Google Cloud Composer環境で特定の`google-cloud-pubsub`ライブラリバージョンを明示的に`requirements.txt`などで指定している場合、バージョンアップを検討する際は、これらの変更がアプリケーションの期待する動作に影響を与えないことを確認するためのテストを実施することを推奨します。

用語説明：
*   **`google-cloud-pubsub`**: Google Cloud Pub/Subサービスと対話するためにGoogleが提供する公式のPythonクライアントライブラリです。Pub/Subのメッセージの公開（Publish）や購読（Subscribe）を行う際に使用されます。
*   **`StreamingPullRequest`**: Pub/Subのサブスクリプションからメッセージを効率的に取得するためのプルモードの一つで、クライアントとサービス間で長期的なストリーミング接続を維持し、メッセージをリアルタイムに受け取ることができます。
*   **Google Cloud Composer**: Google Cloud上でApache Airflowをフルマネージドで実行できるサービスです。ワークフローのオーケストレーションに利用され、PythonベースのDAGs（Directed Acyclic Graphs）でタスクを定義します。
*   **Apache Airflow**: プログラマティックにワークフローをオーサリング、スケジュール、監視するためのオープンソースプラットフォームです。主にデータパイプラインの構築に利用されます。