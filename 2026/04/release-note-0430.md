
# Title: April 29, 2026 
Link: https://docs.cloud.google.com/release-notes#April_29_2026<br>
Google Cloud のリリースノートに基づき、各製品の変更点、影響有無、および対処方法を調査しました。

---

# BigQuery

## Breaking

原文: Strict act-as mode is enforced globally for all Dataform repositories, requiring the use of a custom service account or user credentials for running Dataform workflows, BigQuery pipelines, notebooks, and data preparations.
[Strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode)

説明：
Dataform の「厳格な act-as モード」が、すべての Dataform リポジトリに対してグローバルに強制されるようになりました。これにより、Dataform ワークフロー、BigQuery パイプライン、ノートブック、およびデータ準備を実行する際には、カスタムサービスアカウントまたはユーザー認証情報を使用することが必須となります。これは、実行環境のセキュリティと権限管理を強化するための変更です。

影響有無：
**影響あり（高）**
この変更は「Breaking」として分類されており、既存の Dataform の設定によっては重大な影響が発生する可能性があります。
これまでカスタムサービスアカウントやユーザー認証情報を明示的に設定せずに Dataform ワークフローを実行していた場合、この変更が適用された後、ワークフローが失敗する可能性があります。特に、デフォルトのサービスアカウントや、権限が適切に分離されていない環境で Dataform を利用している場合は、直ちに影響を受ける可能性があります。

対処方法：
Dataform のワークフローを実行する際に使用する認証情報（実行時のサービスアカウントまたはユーザー認証情報）を、明示的に設定し、必要な権限が付与されていることを確認する必要があります。
1.  **既存の Dataform リポジトリの設定確認:** 現在 Dataform を利用している場合は、各リポジトリの「Execution settings (実行設定)」を確認し、どの認証情報が使用されているかを確認します。
2.  **カスタムサービスアカウントの作成と付与:**
    *   BigQuery や Cloud Storage などの必要なリソースに対する適切な権限（例: `BigQuery Data Editor`, `BigQuery Job User` など）を持つ新しいサービスアカウントを作成します。
    *   Dataform リポジトリの実行設定において、作成したカスタムサービスアカウントを指定します。
3.  **CI/CD パイプラインの更新:** Dataform を CI/CD パイプラインに組み込んでいる場合、そのパイプラインが適切な認証情報を使用して Dataform コマンドや API を呼び出していることを確認し、必要に応じて設定を更新します。
4.  **詳細ドキュメントの参照:** [Dataform の strict act-as mode のドキュメント](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode)を参照し、具体的な設定手順を確認してください。

用語説明：
*   **Dataform:** BigQuery 上でのデータ変換とパイプライン構築を SQL ベースで自動化するための Google Cloud サービス。データのバージョン管理、テスト、ドキュメンテーションなどの機能を提供する。
*   **act-as mode (偽装モード):** Google Cloud IAM (Identity and Access Management) の機能の一つで、あるプリンシパル（ユーザー、サービスアカウントなど）が、別のサービスアカウントの権限を一時的に借用して操作を実行する機能。これにより、権限の委譲と分離が可能になる。
*   **Strict act-as mode (厳格な act-as モード):** `act-as mode` の一種で、実行時の認証情報が明示的に指定された場合にのみ操作を許可するセキュリティ強化機能。デフォルトの認証情報や、意図しない権限の借用を防ぐ。
*   **Service Account (サービスアカウント):** Google Cloud リソースにアクセスするために、アプリケーションや仮想マシン、その他の Google Cloud サービスが使用する特別なアカウント。人間がログインするユーザーアカウントとは異なる。
*   **User Credentials (ユーザー認証情報):** Google Cloud にアクセスするための個々のユーザーアカウントの認証情報。

---

# Google Kubernetes Engine

## Fixed

原文: In GKE versions earlier than 1.34.6-gke.1154000 and 1.35.2-gke.1691000, mounting Cloud Storage buckets by using the Cloud Storage FUSE CSI driver can experience significant delays. This issue typically manifests as a `CreateContainer error` that states the following message: `failed to reserve container name`. This error is self-healing and resolves automatically after the underlying mount operation completes and the container runtime releases the reservation. The delay is caused by an inefficient bucket access check performed by the CSI driver sidecar by using the `ListObjects` API method, which can take several hours to complete on buckets that contain millions of empty folders. The error occurs because the `kubelet` enforces a strict two-minute timeout for the container creation request. If the FUSE mount process exceeds this time limit while the sidecar is performing the initial bucket access check, then the `kubelet` cancels the operation and retries. However, the container runtime remains blocked on the first attempt and retains the reservation for the container name. The new GKE releases fix this issue by replacing the `ListObjects` check with the `GetStorageLayout` API method, which performs the same validation but returns almost instantly in most cases. To resolve this issue, upgrade your cluster to one of the following versions: 1.34.6-gke.1154000 or later, 1.35.2-gke.1691000 or later. For GKE version 1.33 clusters running version 1.33.5-gke.2435000 or later, you can mitigate this issue by setting the `skipCSIBucketAccessCheck: "true"` volume attribute to bypass the check. There is no supported fix for this issue in cluster versions 1.33.5-gke.2435000 and earlier.

説明：
GKE の特定の古いバージョン（1.34.6-gke.1154000 より前、および 1.35.2-gke.1691000 より前）において、Cloud Storage FUSE CSI ドライバを使用して Cloud Storage バケットをマウントする際に、著しい遅延が発生する問題が修正されました。この問題は、数百万もの空のフォルダを含むバケットに対して `ListObjects` API メソッドによる非効率なバケットアクセスチェックが実行されることが原因で、コンテナ作成時に `CreateContainer error: failed to reserve container name` というエラーが発生することがありました。このエラーは自己回復するものの、`kubelet` がコンテナ作成リクエストに2分間のタイムアウトを課しているため、マウント処理がこの時間を超えると、コンテナ作成が中断・再試行され、コンテナ名の予約が解放されないままになることがありました。
新しい GKE リリースでは、この非効率な `ListObjects` チェックを `GetStorageLayout` API メソッドに置き換えることで、問題を解決し、ほぼ瞬時に検証が完了するようになりました。

影響有無：
**影響なし（ただし、該当する利用状況であれば改善の恩恵あり）**
このリリースは「Fixed」カテゴリであり、既存の構成に直接的な悪影響を与えるものではありません。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) の利用について:** Cloud Composer は内部で GKE を基盤としていますが、通常、ユーザーが直接 Cloud Storage FUSE CSI ドライバを使用して Pod にバケットをマウントするケースは一般的ではありません。Airflow DAG やプラグインで明示的にこのようなマウントを行っていない限り、この問題による直接的な影響は限定的であると考えられます。もし、カスタムで GCS FUSE CSI ドライバを使用しているワークロードが Composer の基盤 GKE クラスター上で稼働している場合、影響を受ける可能性があります。

もし貴社の GKE クラスターが上記の脆弱なバージョンに該当し、かつ Cloud Storage FUSE CSI ドライバを用いて、特に多数の空フォルダを含む Cloud Storage バケットをマウントしている場合に、この問題（コンテナ作成の遅延やエラー）に遭遇している可能性があります。その場合は、この修正によりシステムの安定性とパフォーマンスが向上します。現状、問題が発生していない場合は、この修正による直接的な機能改善の恩恵は少ないですが、将来的な安定性向上のためにもバージョンアップを検討すべきです。

対処方法：
現在の GKE クラスターが上記の問題に該当するバージョン（1.34.6-gke.1154000 より前、または 1.35.2-gke.1691000 より前）である場合、以下のいずれかの方法で問題を解決または軽減できます。
1.  **GKE クラスターのアップグレード:** クラスターを以下のいずれかのバージョンにアップグレードすることを強く推奨します。
    *   `1.34.6-gke.1154000` またはそれ以降
    *   `1.35.2-gke.1691000` またはそれ以降
2.  **一時的な軽減策（GKE 1.33 の場合）:** GKE バージョン `1.33.5-gke.2435000` 以降の 1.33 クラスターを使用している場合、Cloud Storage FUSE CSI ドライバのボリューム属性に `skipCSIBucketAccessCheck: "true"` を設定することで、問題を軽減できます。ただし、これは一時的な回避策であり、根本的な解決のためにはアップグレードが推奨されます。
3.  **非対応バージョンへの注意:** GKE バージョン `1.33.5-gke.2435000` 以前の 1.33 クラスターには、この問題に対するサポートされている修正がないため、速やかにアップグレードを検討してください。
4.  **Google Cloud Composer2 の場合:** Composer の基盤となる GKE バージョンは Google によって管理されています。Composer 環境のメンテナンスウィンドウ中に自動的に GKE バージョンがアップグレードされる可能性があります。もしこの問題に起因すると思われる挙動が確認された場合は、Composer の現在のGKEバージョンを確認し、必要に応じて Composer のサポートに問い合わせるか、最新の Composer バージョンへのアップグレードを検討してください。

用語説明：
*   **Google Kubernetes Engine (GKE):** Google Cloud 上でコンテナ化されたアプリケーションをデプロイ、管理するためのマネージド Kubernetes サービス。
*   **Cloud Storage FUSE CSI driver:** Kubernetes の Pod から Cloud Storage バケットにファイルシステムとしてアクセスできるようにする CSI (Container Storage Interface) ドライバ。これにより、アプリケーションは Cloud Storage をあたかもローカルファイルシステムのように扱える。
*   **CSI (Container Storage Interface):** Kubernetes が様々なストレージシステム（ブロックストレージ、ファイルストレージなど）と連携するための標準インターフェース。
*   **kubelet:** 各 Kubernetes ノード上で動作するエージェントで、Pod のライフサイクル管理（コンテナの起動・停止）、ボリュームのマウント、ノードの状態報告などを担当する。
*   **ListObjects API method:** Cloud Storage バケット内のオブジェクト（ファイルやフォルダ）の一覧を取得するための Google Cloud Storage API。多数のオブジェクトがあるバケットでは、この操作に時間がかかることがある。
*   **GetStorageLayout API method:** Cloud Storage バケットのストレージレイアウト情報を取得するための Google Cloud Storage API。`ListObjects` よりも効率的にバケットの存在確認や構造の取得を行うことができる。
# Title: April 28, 2026 
Link: https://docs.cloud.google.com/release-notes#April_28_2026<br>
# AlloyDB for PostgreSQL
## Change
原文: When the initial user or password is unspecified during cluster creation, a locked `postgres` role with `null` password is created.

[`postgres` role](https://docs.cloud.google.com/alloydb/docs/database-users/overview#postgres-user)

説明：
AlloyDB for PostgreSQLにおいて、新規クラスター作成時に初期ユーザーやパスワードが指定されなかった場合、デフォルトの`postgres`ロールが「ロックされた」状態で、「パスワードなし（null password）」として作成されるようになりました。これにより、意図せずデフォルトの`postgres`ロールが使用可能な状態になることを防ぎ、セキュリティが強化されます。

影響有無：
**影響はありません。**
この変更は、新規クラスター作成時のデフォルトの挙動に関するものであり、既存のAlloyDBクラスターには影響しません。また、新規クラスターを作成する際も、ベストプラクティスとして初期ユーザーとパスワードを明示的に指定することが推奨されており、通常はこの変更の影響を受けることはありません。セキュリティ上の理由から、`postgres`ロールを直接使用するのではなく、作成時に付与される`cloudsqlsuperuser`権限を持つユーザーを管理に利用することが推奨されます。

対処方法：
特別な対処は不要です。
新規にAlloyDBクラスターを作成する際は、セキュリティのベストプラクティスに従い、初期ユーザー名とパスワードを必ず指定してください。これにより、ユーザーが意図しない状態で`postgres`ロールが使用不能になることを心配する必要がなくなります。

用語説明：
*   **`postgres` role**: PostgreSQLデータベースシステムにおけるデフォルトのスーパーユーザーロールです。このロールは、データベース内のすべての権限を持ち、システム管理タスクを実行できます。セキュリティ上の理由から、日常的な操作やアプリケーションからの接続には、このロールを直接使用せず、より制限された権限を持つ専用のユーザーロールを作成することが推奨されます。
*   **`locked` role**: データベースのロール（ユーザー）がロックされている状態を指します。ロックされたロールでは、パスワードが設定されていても、そのロールを使ってデータベースにログインすることはできません。この機能は、アカウントの一時的な無効化やセキュリティ強化のために使用されます。
*   **`null` password**: パスワードが設定されていない状態を指します。通常、パスワードがnullの場合、パスワードなしでログインが許可される場合と、ログインができない場合があります。今回の文脈では「`locked`」と組み合わされることで、この`postgres`ロールではログインできない状態が確保されていることを示します。
# Title: April 27, 2026 
Link: https://docs.cloud.google.com/release-notes#April_27_2026<br>
Google Cloudのリリースノートに関する影響調査の結果を以下に報告します。

---

# API Gateway

## Change

原文:
**New validations on paths in API configurations**

 API Gateway now enforces stricter syntax validations on templated paths when you create new API configurations and gateways.

 See path templating syntax rules and limits for more information.

[path templating syntax rules](https://docs.cloud.google.com/api-gateway/docs/path-templating#syntax_rules)
[limits](https://docs.cloud.google.com/api-gateway/docs/path-templating#limits)

説明:
API Gatewayにおいて、新しいAPI構成またはゲートウェイを作成する際に、パスのテンプレート構文に対する検証ルールが厳格化されました。これまでは許容されていた一部のパス構文が、今後はエラーとして扱われる可能性があります。詳細な構文ルールについては、提供されたリンク先のドキュメントを参照してください。

影響有無:
**あり**。
既存のデプロイ済みAPI Gateway構成には直接的な影響はありません。しかし、**今後新しいAPI構成をデプロイする場合、または既存のAPI構成を更新して再デプロイする場合に影響が発生します**。既存のAPIパス定義が新しい厳格な構文ルールに準拠していない場合、デプロイメント時に検証エラーが発生し、デプロイが失敗する可能性があります。これは、APIのCI/CDパイプラインや開発ワークフローに影響を与える可能性があります。

対処方法:
新規APIの開発や既存APIの更新を行う前に、[API Gatewayのパスのテンプレート構文ルール](https://cloud.google.com/api-gateway/docs/path-templating#syntax_rules) および [制限](https://cloud.google.com/api-gateway/docs/path-templating#limits) を確認し、現在および将来のAPIパスがこれらの新しい要件に準拠していることを確認してください。
もし既存のAPI構成で新しいルールに準拠していないパスがある場合は、必要に応じてパス定義の修正を検討してください。また、APIデプロイメントのCI/CDパイプラインに、これらの構文ルールに合致するかを検証するステップを追加することも有効です。

用語説明:
*   **API Gateway:** Google Cloud上でAPIを安全に公開、管理、保護するためのフルマネージドサービスです。バックエンドサービス（Cloud Functions, Cloud Run, App Engineなど）へのトラフィックをルーティングし、認証、認可、レート制限などを適用する機能を提供します。
*   **Path templating (パスのテンプレート化):** APIエンドポイントのパスを定義する際に使用される形式で、パス変数（例: `/users/{user_id}`）を含むことができます。これにより、単一のAPIパスで複数のリソースや動的なコンテンツに対応させることができます。

---

# Cloud Service Mesh

## Announcement

原文:
Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation in the
regular channel now supports a limited implementation of the `EnvoyFilter` API.
To learn about the supported fields, extensions, and how to use `EnvoyFilter`
for features like local rate limiting see
Data plane extensibility with `EnvoyFilter`.

[Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility)
 To troubleshoot any issue while configuring, see
Resolving data plane extensibility issues.

[Resolving data plane extensibility issues](https://docs.cloud.com/service-mesh/docs/troubleshooting/troubleshoot-data-plane-extensibility)

説明:
マネージドCloud Service Mesh（Traffic Directorをデータプレーンに利用する実装）のレギュラーチャネルにおいて、`EnvoyFilter` APIの限定的な実装がサポートされるようになりました。これにより、ユーザーはEnvoyプロキシの動作をより詳細にカスタマイズできるようになり、特にローカルレートリミットのようなデータプレーンの拡張機能を活用できるようになります。サポートされるフィールドや拡張機能の詳細、および使用方法については、提供されたリンク先のドキュメントを参照してください。

影響有無:
**なし (直接的な影響)**。
この変更は、既存のCloud Service Meshの動作に破壊的な影響を与えるものではなく、**新しい機能の追加**です。現在デプロイされているサービスや構成はこれまで通り動作し続けます。
ただし、今後データプレーンのカスタマイズや特定の要件を満たすために`EnvoyFilter`の利用を検討する際には、この新機能が選択肢となり、サービス運用戦略に影響を与える可能性があります。

対処方法:
現時点で特別な対処は不要です。
しかし、将来的にEnvoyプロキシの特定の動作を調整したい場合や、サービスメッシュ内でローカルレートリミットなどのカスタムポリシーを適用したい場合は、この機能を活用することを検討してください。その際は、[データプレーンの拡張性に関するドキュメント](https://cloud.google.com/service-mesh/docs/data-plane-extensibility) を参照し、サポートされるフィールドと拡張機能、および使用方法について理解を深めることを推奨します。

用語説明:
*   **Cloud Service Mesh:** Google Cloudが提供するフルマネージドなサービスメッシュプラットフォームです。サービス間の通信を安全かつ効率的に管理し、オブザーバビリティ、トラフィック管理、セキュリティ機能などを提供します。
*   **Traffic Director:** Google Cloudのマネージドなサービスメッシュコントロールプレーンです。アプリケーション層のロードバランシング、トラフィック管理、ヘルスチェックなどをグローバルに管理します。Envoyプロキシをデータプレーンとして使用することが一般的です。
*   **EnvoyFilter:** Istio（Cloud Service Meshの基盤技術の一つ）のカスタムリソース定義 (CRD) です。データプレーンであるEnvoyプロキシに対して、特定の動作をカスタマイズするための設定を適用するために使用されます。これにより、高度なトラフィックルーティング、カスタムメトリックの収集、セキュリティポリシーの適用などが可能になります。
*   **データプレーン:** サービスメッシュにおいて、サービス間の実際のトラフィックを処理する部分を指します。通常、Envoyプロキシなどのサイドカープロキシがこれに当たります。