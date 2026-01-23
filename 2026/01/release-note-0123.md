
# Title: January 22, 2026 
Link: https://docs.cloud.google.com/release-notes#January_22_2026<br>
Google Cloudのインフラエンジニアとして、BigQueryに関するリリースノートの影響を調査しました。

---

# BigQuery
## Fixed
原文: Support for table parameters in table-valued functions is restored.
[table parameters in table-valued functions](https://docs.cloud.google.com/bigquery/docs/table-functions#table_parameters)

説明：
BigQueryのテーブル値関数（Table-valued functions）において、テーブル全体を引数として渡す「テーブルパラメータ（Table parameters）」の機能のサポートが復元されました。これは、一時的に利用できなかった、または期待通りに動作していなかったこの機能が、再び正常に利用可能になったことを意味します。

影響有無：
**影響なし、またはポジティブな影響**
*   **影響なし:** 現在、構築済みのサービスでテーブルパラメータを持つテーブル値関数を使用していない場合、直接的な影響はありません。
*   **ポジティブな影響:** 過去にこの機能を利用しようとしてエラーが発生していた、または一時的な問題により利用を断念していた場合、その問題が解消され、機能が正常に利用できるようになったため、ポジティブな影響があります。既存のワークロードでこの機能を利用していて問題が発生していた場合は、その問題が解消されます。

対処方法：
特別な緊急対応は不要です。
*   もし過去にテーブルパラメータを持つテーブル値関数の問題により迂回策（workaround）を実装していた場合は、その迂回策を削除し、本来の機能を利用するように見直すことが可能です。
*   新たにこの機能を利用したい場合は、問題なく利用できるようになったことを認識し、今後の開発に組み込むことが可能です。

用語説明：
*   **Table-valued functions (テーブル値関数):** BigQueryを含むSQLデータベースにおいて、ユーザーが定義する関数の一種です。通常の関数が単一のスカラー値（例: 数値、文字列）を返すのに対し、テーブル値関数はSQLの`FROM`句で使用できるテーブル（行と列のセット）を結果として返します。これにより、複雑なデータ変換やロジックを関数として再利用しやすくなります。
*   **Table parameters (テーブルパラメータ):** テーブル値関数に、引数としてテーブル全体を渡す機能です。一般的な関数がスカラー値や配列を引数として取るのに対し、テーブルパラメータを使用すると、別のクエリの結果セットや一時テーブルなどを関数の入力として直接利用できます。BigQueryでは`TABLE`キーワードを用いて指定します。
*   **Fixed (修正済み):** リリースノートにおけるカテゴリの一つで、以前から存在していた不具合や問題が修正され、機能が正常に動作するようになったことを示します。通常、既存のシステムに負の影響を与えることはなく、むしろ安定性や機能性が向上します。
# Title: January 21, 2026 
Link: https://docs.cloud.google.com/release-notes#January_21_2026<br>
Google Cloudのリリースノートに基づき、構築済みのサービスへの影響調査結果を以下に報告します。

---

# AlloyDB for PostgreSQL

## Issue

原文: Automatic IAM authentication is unavailable when you use managed connection pooling with the AlloyDB Auth Proxy and Language Connectors. To sign into your database without a password, use manual IAM authentication. For more information, see Connect using an IAM account

説明：AlloyDB for PostgreSQLにおいて、マネージドコネクションプーリング、AlloyDB Auth Proxy、およびLanguage Connectorsを組み合わせて使用している場合に、自動IAM認証が利用できない問題が発生しています。この構成でパスワードなしでデータベースにサインインするためには、現時点では手動でのIAM認証を使用する必要があります。

影響有無：
*   **影響あり**：AlloyDB for PostgreSQLを使用しており、かつ「マネージドコネクションプーリング」と「AlloyDB Auth ProxyおよびLanguage Connectors」を併用し、「自動IAM認証」を利用している場合に影響があります。
*   Google Cloud Composer2は直接AlloyDB for PostgreSQLを使用するサービスではありませんが、もしAlloyDBをデータベースとして使用するカスタムアプリケーションがComposerのDAGから呼び出されている場合、そのアプリケーションの接続方法に影響が出る可能性があります。
*   既存の運用で自動IAM認証に依存している場合、一時的な運用変更が必要になる可能性があります。

対処方法：
*   該当する構成を使用している場合、当面の間は「Connect using an IAM account」ドキュメントを参照し、手動IAM認証への切り替えを検討してください。
*   この問題が解決されるまでの間、または自動IAM認証が再開されるまでの回避策として、IAM認証を必要としない認証方法（例: パスワード認証）の利用も考慮できますが、セキュリティポリシーとの兼ね合いで慎重に検討してください。

用語説明：
*   **IAM認証 (Identity and Access Management Authentication)**: Google CloudのIAMポリシーと認証情報を使用して、データベースへのアクセスを認証する仕組みです。パスワードを使用せずに、よりセキュアなアクセス管理を可能にします。
*   **マネージドコネクションプーリング (Managed Connection Pooling)**: データベースへの接続をサービス側で管理・再利用することで、アプリケーションの負荷を軽減し、パフォーマンスを向上させる機能です。
*   **AlloyDB Auth Proxy**: AlloyDBへの安全な接続を確立するためのプロキシで、IAM認証をサポートします。
*   **Language Connectors**: 特定のプログラミング言語（Python, Java, Goなど）からAlloyDBに接続するためのGoogle提供のライブラリやドライバーです。

---

# Apigee X

## Security

原文: Security fix for Apigee infrastructure. This addresses the following vulnerabilities:- CVE-2025-68161- CVE-2025-67735-... (and other CVEs)

説明：Apigeeのインフラストラクチャにおいて、複数のセキュリティ脆弱性（CVE-2025-68161, CVE-2025-67735など多数）に対するセキュリティ修正が適用されました。

影響有無：
*   **影響なし**：Apigee Xはマネージドサービスであり、このセキュリティ修正はGoogle Cloud側で自動的に適用されます。ユーザー側で特別な操作は不要であり、基盤のセキュリティが強化されるため、サービス運用の安全性向上に寄与します。

対処方法：
*   特別な対処は不要です。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: サイバーセキュリティの脆弱性に対して割り当てられる国際的な識別子です。
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームで、APIの設計、セキュアな公開、分析、監視などをサポートします。

## Fixed

原文: Implemented full TLS validation when fetching JWKS from remote URIs

説明：リモートURIからJWKS（JSON Web Key Set）を取得する際に、完全なTLS検証が実装されました。

影響有無：
*   **影響なし（ただし、正しくない設定の場合は影響あり）**：Apigeeで外部のJWKS URIを利用している場合、より厳密なTLS検証が行われるようになります。これによりセキュリティが向上しますが、もし参照先のJWKSエンドポイントのTLS設定が不適切であった場合、JWKSの取得が失敗する可能性があります。通常、既存の適切に設定されたAPIプロキシには影響ありません。

対処方法：
*   通常は不要です。もしJWKSの取得に関する問題が発生した場合、参照先のJWKSエンドポイントのTLS証明書が適切に設定されているかを確認してください。

用語説明：
*   **TLS (Transport Layer Security)**: インターネット上の通信を暗号化し、データの盗聴や改ざんを防ぐためのプロトコルです。
*   **JWKS (JSON Web Key Set)**: JSON Web Token (JWT) の署名を検証するために公開鍵のセットをJSON形式で表現したものです。

---

原文: Quota enforcement logic for Server-Sent Events (SSE) updated Quotas for SSE are now calculated strictly for events containing explicit token counts. The quota enforcement logic skips SSE that lack token usage metadata.

説明：Server-Sent Events (SSE) のクォータ適用ロジックが更新されました。今後は、明示的なトークンカウントを含むイベントに対してのみクォータが厳密に計算され、トークン使用メタデータを持たないSSEはクォータ計算からスキップされます。

影響有無：
*   **影響あり**：Apigee XでSSEを利用しており、そのイベントがトークン使用メタデータを含んでいるか否かによって、クォータの計上方法が変わります。これにより、既存のクォータ使用状況のレポートに変化が見られる可能性があります。多くの場合、より正確なクォータ適用となるため改善と見なされますが、意図しないクォータ超過や過少計上が発生しないか確認が必要です。

対処方法：
*   SSEを使用している場合は、クォータの使用状況を監視し、予期せぬ変化がないか確認してください。必要に応じて、アプリケーション側でSSEイベントにトークン使用メタデータを適切に付与することを検討してください。

用語説明：
*   **Server-Sent Events (SSE)**: ウェブブラウザがサーバーからの一方向のリアルタイムイベント通知を受け取るための技術です。
*   **クォータ (Quota)**: Google Cloudサービスが利用できるリソースの上限値です。

---

原文: Updates to security, infrastructure, and libraries.

説明：セキュリティ、インフラストラクチャ、およびライブラリに関する一般的な更新が行われました。

影響有無：
*   **影響なし**：Apigee Xの基盤システムの改善であり、ユーザーに直接的な影響はありません。サービスの安定性とセキュリティの向上が期待されます。

対処方法：
*   特別な対処は不要です。

## Announcement

原文: On January 21st, 2026, we released an updated version of Apigee (1-17-0-apigee-1). Note: Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：Apigeeの更新バージョン (1-17-0-apigee-1) がリリースされました。このリリースのロールアウトは現在進行中であり、すべてのGoogle Cloudゾーンで完了するまでに4営業日以上かかる場合があります。そのため、新しい機能や修正がお客様のApigeeインスタンスで利用可能になるまで時間がかかる可能性があります。

影響有無：
*   **影響あり**：新機能や修正がすぐに利用できない可能性があるという情報です。既存のサービス運用に直接的な悪影響はありませんが、最新の機能や修正をすぐに活用したい場合には、ロールアウトの完了を待つ必要があります。

対処方法：
*   Apigeeの新しい機能や修正が必要な場合は、ロールアウトの完了を待機してください。特別なユーザーアクションは不要です。

---

# BigQuery

## Change

原文: BigQuery is now available in the Bangkok (`asia-southeast3`) region.

説明：BigQueryサービスがバンコク (`asia-southeast3`) リージョンで利用可能になりました。

影響有無：
*   **影響なし**：既存のBigQuery利用には直接的な影響はありません。これは新しいリージョンの追加に関するアナウンスです。
*   ただし、もし将来的にタイ国内でのデータローカリティ要件がある場合や、タイからのアクセスにおけるレイテンシー改善のニーズがある場合、新しいリージョンを利用できる選択肢が増えるという点で、ポジティブな影響があります。

対処方法：
*   特別な対処は不要です。必要に応じて、新しいリージョンでのデータセット作成やクエリ実行を検討してください。

用語説明：
*   **リージョン**: Google Cloudリソースが物理的に配置される地理的な場所のことで、複数のゾーンで構成されます。

---

# Google Kubernetes Engine

## Security

原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image.

説明：今回のリリースには、更新されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらの更新されたイメージには、前回のGKEリリース以降にリリースされたすべてのCOSバージョンからのセキュリティ修正が累積的に含まれています。各COSイメージで解決された特定の脆弱性については、関連するCOSのセキュリティリリースノートを参照してください。

影響有無：
*   **影響なし（ただし、セキュリティ向上のメリットあり）**：GKEノードの基盤となるOSイメージが更新され、セキュリティが向上します。既存のGKEクラスターで自動アップグレードが有効になっている場合、または手動でクラスターをアップグレードする際に、これらの新しいCOSイメージが適用されます。ユーザー側での直接的な作業は不要ですが、クラスターのセキュリティ体制が強化されます。
*   Google Cloud Composer2は内部でGKEを利用しているため、Composer2のノードイメージもこれらの更新されたCOSイメージを使用するようになる可能性があり、その場合、Composer2の基盤のセキュリティも向上します。

対処方法：
*   GKEクラスターの自動アップグレードが有効になっていることを確認してください。自動アップグレードが無効な場合は、計画的にGKEクラスターをアップグレードすることを検討してください。
*   特定のCOSバージョンで修正された脆弱性の詳細を確認したい場合は、提供されたリンク先のCOSリリースノートを参照してください。

用語説明：
*   **Container-Optimized OS (COS)**: Googleが提供する、コンテナワークロードの実行に最適化された最小限のオペレーティングシステムです。GKEのノードイメージとしてよく利用されます。

## Change

原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. ... (Extended, Rapid, Regular, Stableチャンネルでのバージョン変更に関する詳細な記述)

説明：Google Kubernetes Engine (GKE) の各リリースチャンネル（Extended, Rapid, Regular, Stable）において、新しいGKEバージョンが利用可能になり、一部の古いバージョンが利用不可になりました。また、クラスター作成時のデフォルトバージョンが更新され、自動アップグレードのターゲットバージョンも変更されました。これらの変更のロールアウトには、すべてのGoogle Cloudゾーンで完了するまでに数日かかる場合があります。

影響有無：
*   **影響あり**：
    *   **既存のGKEクラスター**: 利用しているリリースチャンネルと現在のバージョンによります。自動アップグレードが有効なクラスターは、設定されたメンテナンスウィンドウや除外期間に従って、新しいパッチバージョンまたはマイナーバージョンへのアップグレードが自動的に行われます。これにより、セキュリティ修正や機能改善が適用されますが、マイナーバージョンアップグレードには非推奨APIの削除など、非互換性のある変更が含まれる可能性があるため、ワークロードへの影響を評価する必要があります。
    *   **新規クラスターの作成**: 新規にGKEクラスターを作成する場合、デフォルトのバージョンが変更されます。
    *   **Google Cloud Composer2への影響**: Composer2は内部でGKEクラスターを利用しています。Composer2のノードはGoogle Cloudによって自動的に管理・アップグレードされるため、これらのGKEバージョン更新はComposer2の基盤の安定性とセキュリティ向上に寄与します。通常、Composer2のユーザーがGKEクラスターを直接操作する必要はありませんが、基盤の変更として理解しておくべきです。Composer2のバージョンアップサイクルはGoogle側で管理され、サポートされるAirflowおよびComposerのバージョンに影響を与える可能性があります。

対処方法：
*   **現状確認**: 運用中のGKEクラスターのバージョン、リリースチャンネル、自動アップグレード設定、メンテナンスウィンドウ/除外期間を確認してください。
*   **計画的なアップグレード**: 自動アップグレードを有効にしている場合でも、本番環境の重要なワークロードを持つクラスターについては、アップグレード前にテスト環境で十分な検証を行うことを強く推奨します。特に、マイナーバージョンアップグレード（例: 1.28から1.29へのアップグレード）が含まれる場合は、非推奨APIの使用がないか、アプリケーションの互換性をKubernetesの変更ログと照らし合わせて確認してください。
*   **Composer2ユーザー**: Composer2のGKE基盤の更新はGoogle側で管理されるため、特別な操作は不要です。Composer2のリリースノートで、サポートされるAirflowおよびComposerのバージョンを確認し、利用しているAirflowのバージョンに合わせた互換性のある変更が提供されているかを確認してください。

用語説明：
*   **リリースチャンネル**: GKEクラスターのアップグレードの頻度と安定性を制御するための設定です。主にStable, Regular, Rapid, Extendedの4種類があります。
*   **自動アップグレード**: GKEがクラスターのコントロールプレーンおよびノードを自動的に最新の推奨バージョンに更新する機能です。
*   **メンテナンスウィンドウ**: GKEが自動アップグレードやその他のメンテナンス作業を実行してもよい時間帯を設定する機能です。
*   **メンテナンス除外期間**: GKEが自動アップグレードやメンテナンス作業を実行してはならない期間を設定する機能です。これにより、特定の期間（例: 繁忙期）のサービス停止リスクを回避できます。
# Title: January 20, 2026 
Link: https://docs.cloud.google.com/release-notes#January_20_2026<br>
Google Cloudのリリースノートに基づき、構築済みのサービスへの影響有無を調査し、以下の通り回答いたします。

---

# Cloud Logging
## Announcement
原文: Cloud Logging adds support for the `asia-southeast3` region. For a complete list of supported regions, see Supported regions.
説明: Cloud Loggingが、新しいリージョンである `asia-southeast3` (シンガポール) でのログバケット作成とログデータ保存をサポートするようになりました。これにより、このリージョンにデプロイされたリソースのログを、より地理的に近い場所にあるLoggingバケットに保存できるようになります。
影響有無: 影響なし
理由: 新しいリージョンサポートの追加であり、既存のログ保存設定やアプリケーションの動作に直接的な変更や影響を与えるものではありません。
対処方法: 不要
用語説明:
*   `asia-southeast3`: Google Cloudが提供するリージョンの一つで、地理的にはシンガポールに位置します。
*   ロギングバケット (Logging bucket): Cloud Loggingにおいて、収集されたログデータを保存するためのストレージリソースです。リージョンごとに作成・管理されます。

---

# Cloud Service Mesh
## Announcement
原文: **1.27.5-asm.0 is now available for in-cluster Cloud Service Mesh.** You can now download 1.27.5-asm.0 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.27.5 subject to the list of supported features. Cloud Service Mesh version 1.27.5-asm.0 uses envoy v1.35.9-dev.
説明: in-cluster Cloud Service Meshの新しいバージョン `1.27.5-asm.0` が利用可能になりました。このバージョンは、オープンソースのIstio 1.27.5の機能をベースにしており、Envoyのバージョンは `v1.35.9-dev` を使用しています。
影響有無: 影響あり（潜在的）
理由: 現在in-cluster Cloud Service Meshを利用している場合、より新しいバージョンへのアップグレードを検討する選択肢が追加されます。新バージョンにはIstioの機能改善やバグ修正が含まれる可能性がありますが、アップグレードには計画とテストが必要です。既存のシステムに自動的に適用される変更ではありません。
対処方法: Cloud Service Meshを利用している場合、新バージョンの機能や変更点を確認し、アップグレードを検討してください。アップグレード前には、テスト環境での十分な検証と、Google Cloudが提供するアップグレードガイドに従うことを推奨します。
用語説明:
*   in-cluster Cloud Service Mesh: Google Kubernetes Engine (GKE) クラスタ内にService Meshのコントロールプレーンをデプロイし、ユーザーが管理する形態のCloud Service Meshです。
*   Istio: マイクロサービス間のトラフィック管理、セキュリティ、可観測性を提供するオープンソースのサービスメッシュプラットフォームです。
*   Envoy: Istioのデータプレーンとして使用される、高性能なオープンソースのサービスプロキシです。

## Announcement
原文: **1.28.2-asm.4 is now available for in-cluster Cloud Service Mesh.** You can now download 1.28.2-asm.4 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.28.0 subject to the list of supported features. The following environment variables, fields, and annotations are not supported: [...] Istio dual stack is not supported. Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported. The `ENABLE_AUTO_SNI` flag is still supported to stay aligned with legacy behavior. For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.28.2-asm.4 uses Envoy v1.36.5-dev.
説明: in-cluster Cloud Service Meshのさらに新しいバージョン `1.28.2-asm.4` が利用可能になりました。このバージョンはIstio 1.28.0をベースにしており、Envoyのバージョンは `v1.36.5-dev` を使用しています。また、いくつかの特定の環境変数、フィールド、アノテーション、Istioのデュアルスタック機能、および実験的なEnvoy統計機能はサポート対象外であることが明記されています。ただし、`ENABLE_AUTO_SNI` フラグはレガシーな動作との整合性を保つために引き続きサポートされます。
影響有無: 影響あり（潜在的）
理由: 現在in-cluster Cloud Service Meshを利用している場合、このバージョンへのアップグレードを検討する選択肢が追加されます。特に、**リリースノートで明示的に「サポート対象外」とされている機能や設定を既存の環境で利用している場合は、アップグレード前にそれらを修正または代替手段を検討する必要があります。** これは互換性の問題を引き起こす可能性があります。
対処方法: Cloud Service Meshを利用している場合、新バージョンの機能や変更点を確認し、アップグレードを検討してください。特に、リリースノートに記載されている**サポート対象外の項目（`PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`、`HTTPCookie`の追加属性、`caCertCredentialName`フィールド、`NetworkPolicy`、`shadow host suffix`、`MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP`、Istioデュアルスタック、Envoy統計の実験的機能）を既存の環境で利用していないか厳密に確認してください。** 利用している場合は、アップグレード前にこれらの機能を無効化するか、代替手段を導入する必要があります。アップグレードは十分なテストと計画をもって実施してください。
用語説明:
*   Istio dual stack: IstioがIPv4とIPv6の両方のアドレスを同時に処理する機能です。
*   `ENABLE_AUTO_SNI`: Server Name Indication (SNI) の自動検出を有効にするフラグです。

## Announcement
原文: In-cluster Cloud Service Mesh 1.25 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions.
説明: in-cluster Cloud Service Meshのバージョン `1.25` がサポート対象外となりました。他のバージョンのサポート終了日については、Google CloudのSupported versionsドキュメントを参照するよう促しています。
影響有無: 影響あり（大）
理由: 現在、in-cluster Cloud Service Meshのバージョン `1.25` を利用している場合、このバージョンはサポート対象外となり、セキュリティパッチやバグ修正が提供されなくなります。これにより、運用上のリスクやセキュリティ脆弱性の問題が発生する可能性があります。
対処方法: **現在in-cluster Cloud Service Mesh 1.25を利用している場合は、サポートされている最新バージョン（例: `1.27.5-asm.0` や `1.28.2-asm.4`）への速やかなアップグレードが必須です。** アップグレード手順については、Google Cloudのドキュメントを参照し、本番環境適用前に十分なテストを実施してください。
用語説明:
*   Supported versions: Google Cloudのプロダクトやサービスがサポートを提供する期間や条件を定義したドキュメントです。

## Announcement
原文: **1.26.8-asm.1 is now available for in-cluster Cloud Service Mesh.** You can now download 1.26.8-asm.1 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.26.8 subject to the list of supported features. Cloud Service Mesh version 1.26.8-asm.1 uses envoy v1.34.11.
説明: in-cluster Cloud Service Meshのバージョン `1.26.8-asm.1` が利用可能になりました。このバージョンはIstio 1.26.8をベースにしており、Envoyのバージョンは `v1.34.11` を使用しています。
影響有無: 影響あり（潜在的）
理由: 現在in-cluster Cloud Service Meshを利用している場合、より新しいバージョンへのアップグレードを検討する選択肢が追加されます。新バージョンにはIstioの機能改善やバグ修正が含まれる可能性がありますが、アップグレードには計画とテストが必要です。既存のシステムに自動的に適用される変更ではありません。
対処方法: Cloud Service Meshを利用している場合、新バージョンの機能や変更点を確認し、アップグレードを検討してください。アップグレード前には、テスト環境での十分な検証と、Google Cloudが提供するアップグレードガイドに従うことを推奨します。

---

# Google Kubernetes Engine
## Issue
原文: In some GKE versions earlier than 1.34.0-gke.2011000, using the Cloud Storage FUSE CSI driver with streaming writes enabled might cause file writes to fail with an Input/Output error on the application side accompanied by 503 errors in the gke-gcsfuse-sidecar logs. This issue occurs when streaming writes are enabled, and is caused by stalls during write operations. Streaming writes are enabled by default in GKE versions 1.33.2-gke.4655000 and later. To work around this limitation, you can perform one of the following actions: Upgrade your cluster to GKE version 1.34.1-gke.3849001 or later. If you can't upgrade your cluster, disable streaming writes by passing the `--enable-streaming-writes=false` or `write:enable-streaming-writes:false` flags when you configure mount options for Cloud Storage FUSE CSI driver. These flags only prevent error reliably when staging writes use fast media types such as SSD or tmpfs. tmpfs is specified using `--temp-dir` or `file-system:temp-dir` flags when you configure mount options.
説明: 特定のGKEバージョン（`1.34.0-gke.2011000` より古いもの）において、Cloud Storage FUSE CSIドライバーのストリーミング書き込み機能が有効な場合、アプリケーション側でファイル書き込みエラー（Input/Output error）が発生し、関連する `gke-gcsfuse-sidecar` のログに503エラーが記録される可能性がある問題が報告されています。この問題は書き込み操作中の停止が原因で発生し、GKEバージョン `1.33.2-gke.4655000` 以降ではストリーミング書き込みがデフォルトで有効になっています。回避策として、GKEクラスタを新しいバージョン（`1.34.1-gke.3849001` 以降）にアップグレードするか、ストリーミング書き込みを無効にするオプションをマウント時に指定することが可能です。ただし、ストリーミング書き込みの無効化は、SSDやtmpfsなどの高速メディアタイプを使用する場合にのみ確実にエラーを防げるとのことです。
影響有無: 影響あり（条件付き）
理由: 以下の全ての条件を満たす場合に、アプリケーションのファイル書き込みに失敗する可能性があります。
*   GKEクラスタのバージョンが `1.34.0-gke.2011000` よりも古い。
*   Cloud Storage FUSE CSIドライバーを使用している。
*   ストリーミング書き込みが有効になっている（GKEバージョン `1.33.2-gke.4655000` 以降ではデフォルトで有効）。
対処方法:
1.  **最優先の推奨事項**: GKEクラスタを**バージョン `1.34.1-gke.3849001` 以降にアップグレードしてください**。
2.  **代替策（直ちにアップグレードできない場合）**: Cloud Storage FUSE CSIドライバーのマウントオプションに、ストリーミング書き込みを無効にするフラグ (`--enable-streaming-writes=false` または `write:enable-streaming-writes:false`) を追加してください。この回避策は、ステージング書き込みにSSDやtmpfsなどの高速メディアを使用している場合に最も効果的です。
用語説明:
*   Cloud Storage FUSE CSI driver: Google Cloud Storage (GCS) バケットをKubernetesクラスタ内のPodにファイルシステムとしてマウントするためのContainer Storage Interface (CSI) ドライバーです。
*   ストリーミング書き込み (Streaming writes): Cloud Storage FUSE CSIドライバーの機能で、アプリケーションが書き込みを完了する前に、バックグラウンドでGCSへのアップロードを開始することで、書き込みパフォーマンスを向上させます。
*   Input/Output error: システムがファイルの読み書き操作を実行できなかったことを示すエラーです。
*   Sidecar: メインのアプリケーションコンテナと共に同じPod内で実行される補助的なコンテナパターンです。`gke-gcsfuse-sidecar` はGCS FUSEの機能をPodに提供します。

---
# Title: January 19, 2026 
Link: https://docs.cloud.google.com/release-notes#January_19_2026<br>
Google Cloud のリリースノート調査結果を以下の通りご報告いたします。

---

# BigQuery
## Breaking
原文: Dataform workflows,
BigQuery notebooks,
pipelines,
and
data preparations
are enforcing strict act-as mode at the project level. To avoid failures and
maintain automatic releases, you must use custom service accounts instead of the
default Dataform service agent across all repositories. You must also grant the
Service Account User role (`roles/iam.serviceAccountUser`) to the default
Dataform service agent and relevant principals. For more information and to
verify act-as permissions, see
Use strict act-as mode.

説明：
Dataform workflows、BigQuery notebooks、BigQuery pipelines、および BigQuery data preparations の各機能において、プロジェクトレベルで厳格な「act-asモード」が強制されるようになりました。これにより、既存の設定ではサービスが正常に動作しなくなる可能性があります。
この変更に対応するためには、デフォルトのDataformサービスエージェントではなく、**カスタムサービスアカウントを使用する**必要があります。また、デフォルトのDataformサービスエージェントおよび関連するプリンシパルに対して、`Service Account User`ロール (`roles/iam.serviceAccountUser`) を付与する必要があります。これは、サービスの失敗を防ぎ、自動リリースを維持するために必須の対応となります。

影響有無：**影響あり (Breaking Change)**
BigQueryのDataform、Notebooks、Pipelines、Data Preparationsのいずれかを利用している場合、既存の構成が動作しなくなる可能性があります。特に、デフォルトのDataformサービスエージェントをそのまま利用している環境では、サービスアカウントの権限不足によりジョブやワークフローの実行が失敗する可能性が高いです。

対処方法：
1.  **利用状況の確認:** 現在のプロジェクトでDataform workflows、BigQuery notebooks、BigQuery pipelines、BigQuery data preparationsのいずれかの機能を利用しているか確認してください。
2.  **カスタムサービスアカウントの準備:** 利用している場合、これらの機能で使用するカスタムサービスアカウントを作成、または既存のカスタムサービスアカウントを特定してください。
3.  **ロールの付与:** カスタムサービスアカウントを使用するように設定を更新し、必要に応じて、そのカスタムサービスアカウントにDataformが操作するリソースへの適切な権限（例: BigQuery Data Editor, BigQuery Job Userなど）が付与されていることを確認してください。
4.  **Dataformサービスエージェントへのロール付与:** デフォルトのDataformサービスエージェント（`service-<project-number>@gcp-sa-dataform.iam.gserviceaccount.com`のような形式）に対して、`Service Account User`ロール (`roles/iam.serviceAccountUser`) を付与してください。関連するプリンシパル（例えば、DataformリポジトリにアクセスするユーザーやCI/CDパイプラインのサービスアカウントなど）にもこのロールが付与されているか確認・設定してください。
5.  **公式ドキュメントの参照:** 詳細な手順と厳格な`act-as`モードの要件については、以下の公式ドキュメントを参照し、設定を行ってください。
    *   [Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode)

用語説明：
*   **Dataform workflows:** SQLベースのデータ変換パイプラインを開発、管理、実行するためのGoogle Cloudのサービス。BigQueryと統合され、データウェアハウス内のETL/ELT処理をコードとして管理します。
*   **BigQuery notebooks:** BigQueryデータを分析するために最適化されたJupyterノートブック環境を提供するサービス。PythonやSQLを使用してインタラクティブなデータ分析が可能です。
*   **BigQuery pipelines:** BigQueryデータに対してETL/ELT（抽出、変換、ロード／抽出、ロード、変換）処理を実行するデータパイプラインを構築・管理する機能。主にBigQuery Studio内で利用されます。
*   **BigQuery data preparations:** BigQueryデータの前処理や整形を行うための機能。こちらもBigQuery Studio内で提供されることがあります。
*   **act-as mode (サービスアカウントの権限借用):** あるプリンシパル（ユーザー、サービスアカウントなど）が、別のサービスアカウントの権限を借用して操作を実行する機能。これにより、操作を実行する主体とは異なるサービスアカウントの権限でリソースにアクセスできるようになります。セキュリティと監査の観点から重要です。
*   **`Service Account User`ロール (`roles/iam.serviceAccountUser`):** 指定されたサービスアカウントを借用して、そのサービスアカウントの権限でGoogle Cloudリソースにアクセスすることを許可するIAMロール。

---

# Cloud Logging
## Libraries
原文:
## Java
[3.23.10](https://github.com/googleapis/java-logging/compare/v3.23.9...v3.23.10)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.65.1 (e0ca81e)

[e0ca81e](https://github.com/googleapis/java-logging/commit/e0ca81e148d4f7dd6426640c574b453905cbe000)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.55.1 (#1911) (93eadba)
- Update googleapis/sdk-platform-java action to v2.65.1 (#1910) (3853159)

説明：
Cloud LoggingのJavaクライアントライブラリのバージョン3.23.10がリリースされました。このアップデートには、Javaコードジェネレータ（`gapic-generator-java`）がバージョン2.65.1に更新されたこと、および`com.google.cloud:sdk-platform-java-config`などの依存関係が更新されたことが含まれています。これは主にライブラリ内部の改善や依存関係のアップデートであり、既存のAPIの動作や機能に直接的な変更はありません。

影響有無：**影響なし**
この変更はCloud LoggingのJavaクライアントライブラリの内部的なアップデートであり、既存のGoogle Cloud Composer 2 (Compoer version 2.7.1、Airflow version 2.7.3) の動作に直接的な影響はありません。ComposerはPythonベースであり、このJavaライブラリに直接依存していません。
もし、カスタムでJavaアプリケーションを開発しており、その中でCloud LoggingのJavaクライアントライブラリ（特に旧バージョンを固定して利用している場合）を使用している場合は、最新版へのアップデートを検討することで、内部的な改善や最新の依存関係の恩恵を受けることができます。しかし、強制的な対応は不要です。

対処方法：**不要**
通常の運用においては対応は不要です。
もし、自社開発のJavaアプリケーションでCloud Loggingクライアントライブラリを使用しており、最新の改善を取り入れたい場合は、アプリケーションの依存関係を更新し、ライブラリをバージョン3.23.10にアップグレードすることを検討してください。アップグレードの際には、互換性テストを実施することを推奨します。

用語説明：
*   **Libraries:** 特定のプログラミング言語（この場合はJava）でGoogle Cloudサービスと連携するためのクライアントライブラリやSDKのアップデートを指します。
*   **gapic-generator-java:** Google API Client Libraries for Java（Java用Google APIクライアントライブラリ）を自動生成するためのツールキット。APIの定義に基づいて、言語固有のクライアントコードを生成します。
*   **deps (Dependencies):** ソフトウェアが動作するために必要な他のソフトウェアコンポーネントやライブラリのこと。ここでは、Cloud Logging Javaライブラリが依存している別のライブラリのバージョン更新を指します。
*   **`com.google.cloud:sdk-platform-java-config`:** Google Cloud SDKのJavaプラットフォーム関連の設定や機能を提供するライブラリの一部。