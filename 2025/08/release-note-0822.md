
# Title: August 21, 2025 
Link: https://cloud.google.com/release-notes#August_21_2025<br>
# Google Kubernetes Engine
## Changed
原文: Starting in GKE 1.33.3-gke.1136000, the validation of the
HealthCheckPolicy CRD is now performed earlier by GKE Gateway.
Hence, certain invalid policies are now rejected by `kubectl`. The resulting
error message will specify why the policy is invalid.

説明:
GKEバージョン 1.33.3-gke.1136000 以降、GKE Gateway が `HealthCheckPolicy CRD` のバリデーション（検証）を以前よりも早い段階で実行するようになりました。これにより、構文や定義が誤っている無効な `HealthCheckPolicy` は `kubectl` コマンドによる適用時に拒否されるようになります。拒否された際には、エラーメッセージでポリシーが無効である具体的な理由が示されます。

影響有無:
**影響あり**
GKE Gateway を利用しており、かつ今後 `HealthCheckPolicy` を新規作成または更新する際に、無効なポリシーを適用しようとした場合に影響があります。既存で稼働中の有効な `HealthCheckPolicy` に直接的な影響はありませんが、将来的にポリシーを修正する際に、以前は許容されていた無効な定義が拒否される可能性があります。

対処方法:
`HealthCheckPolicy` を適用する際に `kubectl` でエラーが発生した場合は、表示されるエラーメッセージに従ってポリシー定義を修正してください。この変更は、無効な設定がデプロイされることを防ぎ、設定ミスを早期に発見できるため、運用上の安定性向上に寄与します。

用語説明:
*   **GKE Gateway**: Google Kubernetes EngineでKubernetes Gateway APIを利用するためのコントローラーです。ロードバランシング、トラフィックルーティング、サービスメッシュ連携などを提供します。
*   **HealthCheckPolicy CRD**: Kubernetes Gateway APIのエコシステムの一部として定義されるカスタムリソースです。Gateway APIを通じて公開されるバックエンドサービスに対するヘルスチェックの動作（例: プロトコル、パス、ポート、しきい値など）を詳細に定義するために使用されます。
*   **CRD (Custom Resource Definition)**: KubernetesのAPIを拡張し、ユーザーが独自のオブジェクトタイプ（カスタムリソース）をクラスター内に定義できるようにする機能です。これにより、Kubernetesは組み込みのオブジェクト（Pod, Serviceなど）と同様の方法で、カスタムアプリケーションのコンポーネントを管理できるようになります。
*   **kubectl**: Kubernetesクラスターと対話するためのコマンドラインツールです。リソースのデプロイ、管理、検査など、さまざまな操作に使用されます。
# Title: August 20, 2025 
Link: https://cloud.google.com/release-notes#August_20_2025<br>
# Google Kubernetes Engine

## Fixed

原文: A fix is available for an issue where the `device-fs-monitor` component in the Node Problem Detector generated false `ReadOnlyLocalSSDDetected` warnings on nodes that did not have local SSDs. This could cause customer confusion and distracting warnings. The fix is available in the following GKE versions:
- 1.32.6-gke.1096000 and later
- 1.33.0-gke.1712000 and later

説明:
GKEのNode Problem Detectorコンポーネントに含まれる`device-fs-monitor`が、ローカルSSDを搭載していないノードにおいて誤って`ReadOnlyLocalSSDDetected`という警告を生成する問題が修正されました。この誤検出は、利用者の混乱や不必要な警告を引き起こしていました。この修正は、GKEバージョン1.32.6-gke.1096000以降、および1.33.0-gke.1712000以降で利用可能です。

影響有無:
**影響あり (改善)**
もし現在ご利用中のGKEクラスターが、ローカルSSDを持たないノードで誤った`ReadOnlyLocalSSDDetected`警告を発している場合、この修正を適用することで、不必要な警告が解消され、監視のノイズが減少します。サービスの動作に直接的な悪影響を及ぼすものではなく、監視の健全性が向上します。

対処方法:
現在、ローカルSSDを持たないノードで`ReadOnlyLocalSSDDetected`の誤警告が発生している場合は、GKEクラスターを上記の修正が含まれるバージョン（1.32.6-gke.1096000以降、または1.33.0-gke.1712000以降）にアップグレードすることを推奨します。

用語説明:
*   **Node Problem Detector**: Kubernetesノード上で動作し、ノードのヘルス状態に関する一般的な問題（カーネルのデッドロック、ディスクI/Oエラー、ランタイムの問題など）を検出し、それらをKubernetesイベントとして報告するエージェントです。これにより、ノードの異常を早期に検知し、対処することができます。
*   **`device-fs-monitor`**: Node Problem Detectorを構成するコンポーネントの一つで、ノードのデバイスやファイルシステムの状態を監視する役割を担います。
*   **`ReadOnlyLocalSSDDetected`**: Node Problem Detectorが生成する可能性のある警告イベントの一つです。通常は、ノードに接続されたローカルSSDが何らかの理由で読み取り専用状態になったことを示しますが、この修正ではローカルSSDがないにも関わらず誤ってこの警告が発生する問題に対処しています。
*   **ローカルSSD**: GKEノードに物理的に接続される高速なソリッドステートドライブです。高いI/O性能を提供しますが、一時的なストレージであり、ノードが再起動または削除されるとデータは失われます。永続的なデータ保存には適しません。
# Title: August 18, 2025 
Link: https://cloud.google.com/release-notes#August_18_2025<br>
以下にリリースノートに対する影響調査結果を報告します。

---

# BigQuery
## Changed
原文:
```
## Libraries

 A weekly digest of client library updates from across the Cloud SDK.

[Cloud SDK](https://cloud.google.com/sdk)
## Java

## Changes for google-cloud-bigquery

[google-cloud-bigquery](https://github.com/googleapis/java-bigquery)
[2.54.1](https://github.com/googleapis/java-bigquery/compare/v2.54.0...v2.54.1)
- Adapt graalvm config to arrow update (#3928) (ecfabc4)

[#3928](https://github.com/googleapis/java-bigquery/issues/3928)
[ecfabc4](https://github.com/googleapis/java-bigquery/commit/ecfabc4b70922d0e697699ec5508a7328cadacf8)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 (#3924) (cb66be5)

[#3924](https://github.com/googleapis/java-bigquery/issues/3924)
[cb66be5](https://github.com/googleapis/java-bigquery/commit/cb66be596d1bfd0a5aed75f5a0e36d80269c7f6a)
```
説明：
BigQueryのJavaクライアントライブラリ `google-cloud-bigquery` がバージョン 2.54.1 に更新されました。主な変更点は以下の通りです。
*   GraalVMのコンフィグレーションがApache Arrowのアップデートに対応しました。
*   依存関係である `com.google.cloud:sdk-platform-java-config` がバージョン 3.51.0 に更新されました。

影響有無：
**影響なし**
当社の環境では、Google Cloud Composer 2（Pythonベース）を利用しており、直接Javaクライアントライブラリ `google-cloud-bigquery` を使用していません。この変更はBigQueryサービス本体のアップデートではなく、特定のJavaアプリケーションからBigQueryにアクセスする際に使用されるクライアントライブラリの更新であるため、現状のサービス運用に直接的な影響はありません。

対処方法：
特段の対処は不要です。
もし将来的にJavaで記述されたカスタムアプリケーションが本ライブラリを利用する場合、最新版へのアップデートを検討する際に、これらの変更点が関連するか確認してください。

用語説明：
*   **GraalVM (グラールブイエム)**: 高性能なポリグロット（多言語対応）ランタイム環境です。Javaアプリケーションをネイティブイメージとしてコンパイルすることで、起動時間の短縮やメモリ使用量の削減が期待できます。
*   **Apache Arrow (アパッチアロー)**: インメモリデータ処理のための言語非依存のカラム型データ形式です。異なるシステム間でのデータ転送の効率化や、データ処理性能の向上に寄与します。
*   **クライアントライブラリ**: プログラミング言語（この場合はJava）からGoogle Cloudの各サービス（この場合はBigQuery）のAPIを簡単に呼び出すためのSDK（Software Development Kit）の一部です。

---

# Cloud Storage
## Changed
原文:
```
## Libraries

 A weekly digest of client library updates from across the Cloud SDK.

[Cloud SDK](https://cloud.google.com/sdk)
## Python

## Changes for google-cloud-storage

[google-cloud-storage](https://github.com/googleapis/python-storage)
[3.3.0](https://github.com/googleapis/python-storage/compare/v3.2.0...v3.3.0)
- Add support for bucket IP filter (#1516) (a29073c)

[#1516](https://github.com/googleapis/python-storage/issues/1516)
[a29073c](https://github.com/googleapis/python-storage/commit/a29073cf58df9c5667305e05c6378284057cda23)
- Add logs on AssertionError for issue #1512 (#1518) (6a9923e)

[#1512](https://github.com/googleapis/python-storage/issues/1512)
[#1518](https://github.com/googleapis/python-storage/issues/1518)
[6a9923e](https://github.com/googleapis/python-storage/commit/6a9923e4fc944f7a7c3906eb7800d23677bd2481)
- Update the documentation of move_blob function (#1507) (72252e9)

[#1507](https://github.com/googleapis/python-storage/issues/1507)
[72252e9](https://github.com/googleapis/python-storage/commit/72252e940909ce2e3da9cfd80f5b7b43a026f45c)
```
説明：
Cloud StorageのPythonクライアントライブラリ `google-cloud-storage` がバージョン 3.3.0 に更新されました。主な変更点は以下の通りです。
*   Cloud StorageバケットのIPフィルタリング機能のサポートが追加されました。
*   `AssertionError` 発生時のログ出力が追加され、デバッグ情報が強化されました。
*   `move_blob` 関数のドキュメントが更新されました。

影響有無：
**影響なし**
この変更はCloud Storageサービス本体のアップデートではなく、Pythonクライアントライブラリの更新です。
*   「バケットIPフィルタリングのサポート追加」は新機能の提供であり、既存の利用方法に影響を与えるものではありません。この機能を利用しない限り、既存のワークロードは影響を受けません。
*   「`AssertionError` のログ追加」はデバッグ情報の強化であり、既存の動作を変更するものではありません。
*   「`move_blob` 関数のドキュメント更新」は、関数の動作そのものを変更するものではありません。

当社のGoogle Cloud Composer 2環境では、Pythonベースであるため `google-cloud-storage` ライブラリが内部的に利用される可能性がありますが、これらの変更は破壊的変更ではなく、既存の機能に悪影響を及ぼす可能性は低いと判断されます。

対処方法：
特段の対処は不要です。
*   もし新たにCloud StorageバケットのIPフィルタリング機能を利用する場合は、このライブラリバージョン（またはそれ以降）へのアップデートが必要です。
*   クライアントライブラリのバージョンアップを検討する際は、テスト環境での動作確認を推奨します。

用語説明：
*   **バケットIPフィルタ (Bucket IP Filter)**: Cloud Storageのバケットへのアクセスを、特定のIPアドレスまたはIPアドレス範囲に制限するセキュリティ機能です。これにより、意図しない場所からのアクセスを防ぎ、セキュリティを強化できます。
*   **`AssertionError` (アサーションエラー)**: Pythonプログラムにおいて、開発者が想定した条件が満たされなかった場合に発生するエラーです。通常、プログラムの内部的な整合性チェックに使用されます。
*   **クライアントライブラリ**: プログラミング言語（この場合はPython）からGoogle Cloudの各サービス（この場合はCloud Storage）のAPIを簡単に呼び出すためのSDK（Software Development Kit）の一部です。