
# Title: January 20, 2026 
Link: https://docs.cloud.google.com/release-notes#January_20_2026<br>
以下に、Google Cloudのリリースノートに対する調査結果をまとめました。

---

# Cloud Logging
## Announcement
原文: Cloud Logging adds support for the `asia-southeast3` region. For a complete list of supported regions, see Supported regions.
説明：Cloud Loggingが新しいリージョンである `asia-southeast3` (ジャカルタ) をサポートしました。これにより、ログバケットをこのリージョンに作成できるようになります。
影響有無：影響なし。
既存のログバケットやログの取り込みに直接的な影響はありません。新しいリージョンが追加されただけであり、既存のデプロイメントに影響を与えるものではありません。
対処方法：特になし。
ただし、ログのデータレジデンシー要件などがある場合、今後 `asia-southeast3` リージョンをログの保存先として考慮に入れることが可能になります。
用語説明：
*   **Cloud Logging**: Google Cloudが提供する、アプリケーションやGoogle Cloudサービスから生成されるログを一元的に収集、保存、分析するためのフルマネージドサービスです。
*   **ログバケット (Log Bucket)**: Cloud Loggingでログを保存するための論理的なストレージ単位です。ログバケットは特定のリージョンに紐付けられます。
*   **データレジデンシー (Data Residency)**: データの保存場所に関する規制や要件。特定の地理的地域内にデータを保持する必要がある場合に重要となります。

---

# Cloud Service Mesh
## Announcement
原文: **1.27.5-asm.0 is now available for in-cluster Cloud Service Mesh.** You can now download 1.27.5-asm.0 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.27.5 subject to the list of supported features. Cloud Service Mesh version 1.27.5-asm.0 uses envoy v1.35.9-dev.
説明：in-cluster Cloud Service Meshのバージョン `1.27.5-asm.0` が利用可能になりました。このバージョンにはIstio `1.27.5` の機能が含まれ、Envoy `v1.35.9-dev` を使用しています。
影響有無：影響なし。
これは新しいバージョンの提供開始アナウンスであり、既存のCloud Service Meshのデプロイメントに自動的に適用されるものではありません。現在構築中のGoogle Cloud Composer2はCloud Service Meshを直接利用しないため、影響はありません。
対処方法：特になし。
Cloud Service Meshを利用している場合は、必要に応じてこのバージョンへのアップグレードを検討できます。
用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供するIstioベースのサービスメッシュソリューションです。マイクロサービス間のトラフィック管理、セキュリティ、可観測性を実現します。
*   **in-cluster**: サービスメッシュのコントロールプレーンをKubernetesクラスタ内にデプロイする形態を指します。
*   **Istio**: マイクロサービス接続、管理、セキュリティ、監視のためのオープンソースのサービスメッシュプラットフォームです。
*   **Envoy**: Istioでデータプレーンとして使用される、高性能なオープンソースのL7プロキシです。

---

# Cloud Service Mesh
## Announcement
原文: **1.28.2-asm.4 is now available for in-cluster Cloud Service Mesh.** You can now download 1.28.2-asm.4 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.28.0 subject to the list of supported features. The following environment variables, fields, and annotations are not supported: ... (中略) ... Cloud Service Mesh version 1.28.2-asm.4 uses Envoy v1.36.5-dev.
説明：in-cluster Cloud Service Meshのバージョン `1.28.2-asm.4` が利用可能になりました。このバージョンにはIstio `1.28.0` の機能が含まれ、Envoy `v1.36.5-dev` を使用しています。また、いくつかの環境変数、フィールド、アノテーション、Istioのデュアルスタック機能、およびEnvoy統計情報の実験的な機能はサポートされません。`ENABLE_AUTO_SNI` フラグはレガシー動作との整合性のため引き続きサポートされます。
影響有無：影響なし。
これは新しいバージョンの提供開始アナウンスであり、既存のCloud Service Meshのデプロイメントに自動的に適用されるものではありません。サポートされない機能リストがありますが、これは新規にこのバージョンを導入する、または既存環境をアップグレードする際に考慮すべき点であり、現在の環境に直接的な影響はありません。現在構築中のGoogle Cloud Composer2はCloud Service Meshを直接利用しないため、影響はありません。
対処方法：特になし。
Cloud Service Meshを利用している場合は、このバージョンへのアップグレードを検討できますが、非サポート機能リストに注意が必要です。
用語説明：
*   **デュアルスタック (Dual Stack)**: ネットワークにおいて、IPv4とIPv6の両方を同時にサポートする構成を指します。
*   **SNI (Server Name Indication)**: TLS (Transport Layer Security) 拡張機能の一つで、単一のIPアドレス上で複数のSSL/TLS証明書をホストできるようにします。これにより、クライアントがアクセスしたいサーバー名をTLSハンドシェイク時に指定できます。

---

# Cloud Service Mesh
## Announcement
原文: In-cluster Cloud Service Mesh 1.25 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions.
説明：in-cluster Cloud Service Meshのバージョン `1.25` のサポートが終了しました。他のバージョンのサポート終了日については、関連ドキュメントを参照してください。
影響有無：影響なし。
現在利用中のCloud Service Meshのバージョンが `1.25` でない限り、直接的な影響はありません。現在構築中のGoogle Cloud Composer2はCloud Service Meshを直接利用しないため、影響はありません。
対処方法：
もし貴社の環境でCloud Service Mesh 1.25を利用している場合は、サポート対象バージョンへの速やかなアップグレードを計画・実行してください。サポート終了バージョンはセキュリティパッチやバグ修正が提供されず、セキュリティリスクが高まります。
用語説明：
*   **EOL (End of Life)**: 製品やソフトウェアのサポートが終了する時点を指します。EOL後、通常はバグ修正、セキュリティアップデート、技術サポートが提供されなくなります。

---

# Cloud Service Mesh
## Announcement
原文: **1.26.8-asm.1 is now available for in-cluster Cloud Service Mesh.** You can now download 1.26.8-asm.1 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.26.8 subject to the list of supported features. Cloud Service Mesh version 1.26.8-asm.1 uses envoy v1.34.11.
説明：in-cluster Cloud Service Meshのバージョン `1.26.8-asm.1` が利用可能になりました。このバージョンにはIstio `1.26.8` の機能が含まれ、Envoy `v1.34.11` を使用しています。
影響有無：影響なし。
これは新しいバージョンの提供開始アナウンスであり、既存のCloud Service Meshのデプロイメントに自動的に適用されるものではありません。現在構築中のGoogle Cloud Composer2はCloud Service Meshを直接利用しないため、影響はありません。
対処方法：特になし。
Cloud Service Meshを利用している場合は、必要に応じてこのバージョンへのアップグレードを検討できます。

---

# Google Kubernetes Engine
## Issue
原文: In some GKE versions earlier than 1.34.0-gke.2011000, using the Cloud Storage FUSE CSI driver with streaming writes enabled might cause file writes to fail with an Input/Output error on the application side accompanied by 503 errors in the gke-gcsfuse-sidecar logs. This issue occurs when streaming writes are enabled, and is caused by stalls during write operations. Streaming writes are enabled by default in GKE versions 1.33.2-gke.4655000 and later. To work around this limitation, you can perform one of the following actions: - Upgrade your cluster to GKE version 1.34.1-gke.3849001 or later. - If you can't upgrade your cluster, disable streaming writes by passing the `--enable-streaming-writes=false` or `write:enable-streaming-writes:false` flags when you configure mount options for Cloud Storage FUSE CSI driver. These flags only prevent error reliably when staging writes use fast media types such as SSD or tmpfs. tmpfs is specified using `--temp-dir` or `file-system:temp-dir` flags when you configure mount options.
説明：GKEバージョン `1.34.0-gke.2011000` よりも前の特定のバージョンにおいて、Cloud Storage FUSE CSIドライバでストリーミング書き込みが有効になっている場合、ファイル書き込みが失敗し、アプリケーション側でInput/Outputエラーが発生し、`gke-gcsfuse-sidecar` ログに503エラーが記録される可能性があります。この問題は、書き込み操作中の停止によって引き起こされます。GKEバージョン `1.33.2-gke.4655000` 以降では、ストリーミング書き込みはデフォルトで有効になっています。
影響有無：影響を受ける可能性あり。
Google Cloud Composer2はGKEクラスタ上で動作します。Composer環境でCloud Storage FUSE CSIドライバを明示的に使用しており、かつストリーミング書き込みを有効にしている場合に、この問題に遭遇する可能性があります。特に、Composerが利用しているGKEバージョンが `1.33.2-gke.4655000` 以降であれば、ストリーミング書き込みがデフォルトで有効になっているため、注意が必要です。Composerが内部的にCloud Storage FUSEを使用しているか、またはユーザーがDAGやカスタムプラグインでGoogle Cloud Storage (GCS) をファイルシステムとして利用している場合に影響があります。
対処方法：
1.  **最優先**: GKEクラスタを `1.34.1-gke.3849001` 以降のバージョンにアップグレードすることを推奨します。Google Cloud Composer2の場合、Composerのアップデート（例: 2.7.xからより新しいパッチバージョン）を通じてGKEバージョンも更新されることが多いです。ComposerのGKEバージョンは、Cloud Composerのバージョンとサポートマトリックスで確認してください。
2.  **代替策 (アップグレードが困難な場合)**: Cloud Storage FUSE CSIドライバの設定で、ストリーミング書き込みを無効にしてください。具体的には、CSIドライバのPodまたはPersistentVolumeClaimの構成で `--enable-streaming-writes=false` または `write:enable-streaming-writes:false` フラグをマウントオプションとして追加します。ただし、この回避策は、ステージング書き込みにSSDやtmpfsなどの高速なメディアタイプを使用する場合にのみ確実にエラーを防ぎます。
3.  **確認事項**: 現在利用しているCloud Composer環境のGKEバージョン、およびCloud Storage FUSE CSIドライバの使用状況とストリーミング書き込みの設定を確認してください。
用語説明：
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供する、Kubernetesクラスタを簡単にデプロイ・管理できるマネージドサービスです。
*   **Cloud Storage FUSE CSIドライバ**: Google Kubernetes Engine (GKE) クラスタ内でGoogle Cloud Storage (GCS) バケットをファイルシステムとしてマウントできるようにするKubernetes CSI (Container Storage Interface) ドライバです。これにより、GCS上のファイルをPOSIX互換のファイルシステムとしてアプリケーションからアクセスできます。
*   **CSI (Container Storage Interface)**: Kubernetesなどのコンテナオーケストレーションシステムが、様々なストレージシステム（ブロックストレージ、ファイルストレージ、オブジェクトストレージなど）と連携するための標準インターフェースです。
*   **ストリーミング書き込み (Streaming Writes)**: Cloud Storage FUSE CSIドライバにおける書き込みモードの一つで、ファイルが完全にローカルに書き込まれるのを待たずに、すぐにGoogle Cloud Storageにデータをストリーミングして書き込む方式です。これにより書き込みパフォーマンスが向上しますが、ネットワークや他の要因によっては問題を引き起こす可能性があります。
*   **Input/Output error (I/Oエラー)**: データ読み書き中に発生するエラーで、通常、ストレージデバイスやファイルシステムとの通信問題を示します。
*   **503 Service Unavailable**: HTTPステータスコードの一つで、サーバーが一時的にリクエストを処理できない状態であることを示します。これは通常、過負荷やメンテナンスなどの一時的な問題が原因です。
# Title: January 19, 2026 
Link: https://docs.cloud.google.com/release-notes#January_19_2026<br>
# BigQuery
## Breaking
原文: Dataform workflows, BigQuery notebooks, pipelines, and data preparations are enforcing strict act-as mode at the project level. To avoid failures and maintain automatic releases, you must use custom service accounts instead of the default Dataform service agent across all repositories. You must also grant the Service Account User role (`roles/iam.serviceAccountUser`) to the default Dataform service agent and relevant principals. For more information and to verify act-as permissions, see Use strict act-as mode.

[Dataform workflows](https://docs.cloud.google.com/dataform/docs/sql-workflows)
[BigQuery notebooks](https://docs.cloud.google.com/bigquery/docs/orchestrate-notebooks)
[pipelines](https://docs.cloud.google.com/bigquery/docs/schedule-pipelines)
[data preparations](https://docs.cloud.google.com/bigquery/docs/orchestrate-data-preparations)
[Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode)

説明：
BigQueryのDataformワークフロー、BigQuery Notebooks、BigQueryパイプライン、およびBigQueryデータ準備の各機能において、プロジェクトレベルで「厳密なact-asモード」が強制されるようになりました。
この変更により、障害を回避し、自動リリースを継続するためには、全てのDataformリポジトリでデフォルトのDataformサービスエージェントの使用を避け、カスタムサービスアカウントを使用する必要があります。
また、デフォルトのDataformサービスエージェントおよび関連するプリンシパルに対して、`Service Account User` ロール (`roles/iam.serviceAccountUser`) を付与する必要があります。
詳細およびact-as権限の確認については、提供された公式ドキュメント「Use strict act-as mode」を参照してください。

影響有無：
**影響あり**。
これはBreaking Changeであり、BigQueryのDataformワークフロー、BigQuery Notebooks、BigQueryパイプライン、BigQueryデータ準備機能を使用しているプロジェクトに直接的な影響があります。
これらの機能でデフォルトのDataformサービスエージェントを利用して運用している場合、今回の変更により認証エラーや処理の失敗が発生する可能性があります。特に、自動リリースフローを使用している場合は、その継続性が影響を受けます。

対処方法：
以下の対応が必要です。
1.  **カスタムサービスアカウントの利用への移行**: Dataformワークフロー、BigQuery Notebooks、BigQueryパイプライン、BigQueryデータ準備機能が利用する全てのDataformリポジトリにおいて、デフォルトのDataformサービスエージェントではなく、カスタムサービスアカウントを使用するように構成を変更してください。
2.  **IAMロールの付与**: デフォルトのDataformサービスエージェント（通常は`service-<project-number>@gcp-sa-dataform.iam.gserviceaccount.com`という形式）および、カスタムサービスアカウントに代行させる権限を持つ関連するプリンシパル（例: ユーザー、グループ、他のサービスアカウント）に対して、`Service Account User` ロール (`roles/iam.serviceAccountUser`) を付与してください。
3.  **詳細ドキュメントの参照**: 提供されている公式ドキュメント「[Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode)」を参照し、具体的な設定手順と「act-as」権限の検証方法を確認してください。

用語説明：
*   **Dataform**: Google Cloud上のBigQueryでSQLベースのデータ変換パイプラインを開発、デプロイ、管理するためのサービスです。SQLワークフローのバージョン管理、テスト、オーケストレーションを可能にします。
*   **BigQuery notebooks**: BigQuery Studio内で提供される、Jupyterベースのインタラクティブなノートブック環境です。SQL、Python（BigQuery DataFrames）、Rなどを使用してBigQueryデータを探索、分析、可視化できます。
*   **Pipelines (BigQuery)**: BigQuery Studio内で提供される、データの取り込み、変換、ロード（ETL/ELT）プロセスを自動化するためのワークフローオーケストレーション機能です。
*   **Data preparations (BigQuery)**: BigQuery Studio内で提供される、視覚的なインターフェースを通じてデータのクレンジング、変換、整形を行うための機能です。
*   **act-as mode / 厳密なact-asモード**: Google Cloud IAMにおいて、あるプリンシパル（ユーザーやサービスアカウントなど）が別のサービスアカウントの権限を一時的に借用して操作を実行するメカニズムです。これにより、操作を実行する実際のプリンシパルが、その操作に必要な最小限の権限しか持たなくても、より強力なサービスアカウントの権限を使ってタスクを完了できます。「厳密なact-asモード」が強制されることで、この代行処理がより明示的な権限付与（`Service Account User` ロールなど）を必要とするようになり、セキュリティが強化されます。
*   **Service Account User role (`roles/iam.serviceAccountUser`)**: このIAMロールは、特定のプリンシパル（ユーザー、グループ、または別のサービスアカウント）が、このロールが付与されたサービスアカウントとして操作を実行すること（つまり、サービスアカウントの権限を代行すること）を許可します。