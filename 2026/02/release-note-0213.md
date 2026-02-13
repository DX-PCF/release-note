
# Title: February 11, 2026 
Link: https://docs.cloud.google.com/release-notes#February_11_2026<br>
## Google Kubernetes Engine

### Change
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
説明: Google Kubernetes Engine (GKE) のクラスターバージョンが更新され、新しいバージョンが新規クラスターの作成や既存クラスターのコントロールプレーンおよびノードの手動アップグレードで利用可能になりました。詳細については、GKEのバージョニングとサポート、およびクラスターアップグレードに関するドキュメントを参照してください。
影響有無: **影響なし（将来的な影響の可能性あり）**
現在、お客様のGoogle Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3) 環境は、基盤となるGKEバージョンとして1.27.x系を利用しています。今回のリリースノートで発表されたGKEバージョン (1.32.x, 1.34.x, 1.35.xなど) は、現在のComposer環境のGKEバージョンよりも新しいものです。そのため、即座の直接的な影響はありません。
しかし、Composerはマネージドサービスであり、その基盤となるGKEクラスターはGoogle Cloudによって自動的にアップグレードされます。将来的にComposer環境がこれらの新しいGKEバージョンにアップグレードされる可能性があります。
対処方法:
1.  **ComposerのGKEバージョンアップグレード計画の確認**: Composerは自動的にGKEをアップグレードしますが、今後のGKEバージョンアップグレードがお客様のAirflowワークロードやカスタムコンポーネントに影響を与えないか、Composerのメンテナンスウィンドウ設定を確認してください。
2.  **非推奨APIの確認**: GKEのバージョンアップグレードでは、KubernetesのAPIの非推奨化や削除が行われることがあります。既存のAirflow DAGsやカスタムオペレーター、Kubernetesリソース定義などが非推奨APIを使用していないか事前に確認し、必要に応じて修正を検討してください。

用語説明:
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供する、コンテナ化されたアプリケーションのデプロイ、スケーリング、管理を自動化するマネージドKubernetesサービスです。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスターの管理層であり、クラスターの状態を維持し、Podのスケジューリングやノードの管理を行うコンポーネント群（kube-apiserver, etcd, kube-scheduler, kube-controller-managerなど）を指します。
*   **ノード (Node)**: Kubernetesクラスターにおいて、コンテナ化されたアプリケーション（Pod）を実行するワーカーマシンです。

### Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image. (followed by GKE version and Container-Optimized OS version table)
説明: このリリースには、更新されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらの更新されたイメージには、以前のGKEリリース以降にリリースされたすべてのCOSバージョンからのセキュリティ修正が累積的に適用されています。各COSイメージで解決された具体的な脆弱性については、それぞれのCOSリリースノートを参照してください。
影響有無: **影響なし（ポジティブな影響）**
この変更は、GKEノードの基盤となるOSのセキュリティ強化に関するものです。お客様のComposer環境のGKEノードOSもGoogle Cloudによって管理・更新されるため、将来的にこれらのGKEバージョンへアップグレードされることで、セキュリティ体制が向上します。お客様側での直接的な作業は不要であり、ポジティブな影響のみです。
対処方法: 特になし。Google Cloudの自動アップグレードとセキュリティ管理に任せることで、最新のセキュリティパッチが適用されます。
用語説明:
*   **Container-Optimized OS (COS)**: Google Cloudが提供する、コンテナを実行するために最適化されたLinuxベースのオペレーティングシステムです。GKEクラスターのノードのデフォルトOSとして利用されます。
*   **セキュリティ修正 (Security Fixes)**: ソフトウェアのセキュリティ上の脆弱性（バグや設計上の欠陥）を修正するためのパッチや更新です。

### Change
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - The following versions are now available in the Extended channel: ... - The following versions are no longer available in the Extended channel: ... - Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.29 to 1.30.14-gke.1922000 - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: ...
説明: Extendedチャネルで利用可能なGKEバージョンが更新され、一部の古いバージョンは利用できなくなりました。また、このチャネルで稼働しているクラスターの自動アップグレードターゲットが変更され、メンテナンス除外や非推奨APIの使用など、アップグレードを阻害する要因がない場合、GKEは自動的に指定された新しいマイナーバージョンまたはパッチバージョンへアップグレードを行います。
影響有無: **影響なし**
Google Cloud Composer 2は通常、GKEの「Regular」または「Stable」リリースチャネルを使用します。Extendedチャネルは、長期サポートを必要とする特殊なケースで利用されるチャネルであり、お客様のComposer環境がこのチャネルを使用している可能性は極めて低いです。そのため、この変更による直接的な影響はありません。
対処方法: Composerが現在どのリリースチャネルに属しているかを確認し、Extendedチャネルを利用していないことを確認してください。
用語説明:
*   **GKEリリースチャネル (Release Channel)**: GKEのバージョンアップグレードのペースと安定性を示す設定です。GKEクラスターは特定のチャネルに登録され、そのチャネルのポリシーに従って自動アップグレードされます。主なチャネルにはRapid、Regular、Stable、Extendedがあります。
*   **自動アップグレード (Auto-upgrade)**: GKEクラスターのコントロールプレーンおよびノードが、Google Cloudによって自動的に最新の安定バージョンにアップグレードされる機能です。
*   **メンテナンス除外 (Maintenance Exclusions)**: GKEクラスターの自動アップグレードが実行されない期間を設定する機能です。
*   **非推奨API (Deprecated APIs)**: Kubernetesのバージョンアップに伴い、利用が推奨されなくなり、将来的に削除される可能性のあるAPIです。非推奨APIを使用していると、新しいGKEバージョンへのアップグレードが阻害されたり、アプリケーションが動作しなくなる可能性があります。

### Change
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - The following versions are now available: ... - The following node versions are now available: ... - The following versions are no longer available: ... - Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.32 to 1.33.5-gke.2118001 - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: ...
説明: 利用可能なGKEクラスターおよびノードのバージョンが更新され、一部の古いバージョンは利用できなくなりました。自動アップグレードターゲットも更新され、特定の条件下（メンテナンス除外や非推奨APIの使用がない場合）で、GKEは自動的にマイナーバージョンまたはパッチバージョンへのアップグレードを実施します。
影響有無: **影響なし（将来的な影響の可能性あり）**
前述のGKEバージョン更新アナウンスと同様に、現在のComposer環境 (GKE 1.27.x) はこれらのバージョンを直接利用していないため、即座の影響はありません。しかし、将来的にComposer環境がこれらのバージョンへ自動アップグレードされる可能性があります。
対処方法: 前述の「GKE cluster versions have been updated」のセクションと同様の対処方法を考慮してください。特段、追加の作業は必要ありませんが、Composerの基盤となるGKEが自動アップグレードされる可能性を認識し、ComposerのバージョンとGKEバージョンの互換性を常に確認できるよう準備しておくことが重要です。

### Change
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - Version 1.35.0-gke.2398000 is now the default version for cluster creation in the Rapid channel. - The following versions are now available in the Rapid channel: ... - The following versions are no longer available in the Rapid channel: ... - Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: ... - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: ...
説明: Rapidチャネルでのクラスター作成のデフォルトバージョンが1.35.0-gke.2398000に設定されました。また、Rapidチャネルで利用可能なGKEバージョンが更新され、一部の古いバージョンは利用できなくなりました。このチャネルで稼働しているクラスターの自動アップグレードターゲットも変更されました。
影響有無: **影響なし**
Google Cloud Composer 2は通常、GKEの「Regular」または「Stable」リリースチャネルを使用します。Rapidチャネルは最も早いアップグレードを提供するチャネルであり、Composer環境がこのチャネルを使用している可能性は極めて低いため、この変更による直接的な影響はありません。
対処方法: Composerが現在どのリリースチャネルに属しているかを確認し、Rapidチャネルを利用していないことを確認してください。
用語説明:
*   **Rapidチャネル (Rapid Channel)**: GKEのリリースチャネルの一つで、最も早く最新バージョンが提供されます。新機能やセキュリティパッチを迅速に利用したい場合に選択されますが、安定性よりも新機能の提供が優先されるため、本番環境での利用には慎重な検討が必要です。

### Change
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - The following versions are now available in the Regular channel: ... - Version 1.33.5-gke.2172001 is no longer available in the Regular channel. - Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.32 to 1.33.5-gke.2228001 - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: ...
説明: Regularチャネルで利用可能なGKEバージョンが更新され、一部の古いバージョンは利用できなくなりました。このチャネルで稼働しているクラスターの自動アップグレードターゲットも変更され、特定の条件下（メンテナンス除外や非推奨APIの使用がない場合）で、GKEは自動的に指定された新しいマイナーバージョンまたはパッチバージョンへアップグレードを行います。
影響有無: **影響なし（将来的な影響の可能性あり）**
お客様のComposer環境 (GKE 1.27.x) は、これらのバージョンを直接利用していないため、即座の影響はありません。ただし、Composer 2はRegularチャネルを利用する可能性があるため、将来的にはこれらの新しいバージョンへの自動アップグレードの対象となる可能性があります。自動アップグレードは通常、メンテナンスウィンドウ内で行われるため、サービス停止のリスクは低いですが、アプリケーションの互換性確認は重要となります。
対処方法:
1.  **Composerのメンテナンスウィンドウ設定を確認**: Composerの自動アップグレードはメンテナンスウィンドウ内で実行されます。お客様のシステムに影響が出ないよう、適切なメンテナンスウィンドウを設定していることを確認してください。
2.  **GKEバージョンアップグレードへの備え**: Composerの基盤となるGKEがこれらの新しいバージョンにアップグレードされる可能性を考慮し、お客様のAirflowワークロードやカスタムコンポーネントが新しいGKEバージョンで問題なく動作するかを事前に検証する計画を立ててください。非推奨APIの使用状況も確認し、必要に応じて改修を検討してください。
用語説明:
*   **Regularチャネル (Regular Channel)**: GKEのリリースチャネルの一つで、Rapidチャネルよりも安定性が高く、Stableチャネルよりも新しい機能が早く提供されます。一般的な本番環境での利用に適しています。

### Change
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - Version 1.33.5-gke.2118001 is now the default version for cluster creation in the Stable channel. - The following versions are now available in the Stable channel: ... - The following versions are no longer available in the Stable channel: ... - Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: ... - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: ...
説明: Stableチャネルでのクラスター作成のデフォルトバージョンが1.33.5-gke.2118001に設定されました。また、Stableチャネルで利用可能なGKEバージョンが更新され、一部の古いバージョンは利用できなくなりました。このチャネルで稼働しているクラスターの自動アップグレードターゲットも変更されました。
影響有無: **影響なし（将来的な影響の可能性あり）**
お客様のComposer環境 (GKE 1.27.x) は、これらのバージョンを直接利用していないため、即座の影響はありません。ただし、Composer 2はStableチャネルを利用する可能性があるため、将来的にはこれらの新しいバージョンへの自動アップグレードの対象となる可能性があります。自動アップグレードは通常、メンテナンスウィンドウ内で行われるため、サービス停止のリスクは低いですが、アプリケーションの互換性確認は重要となります。
対処方法:
1.  **Composerのメンテナンスウィンドウ設定を確認**: Composerの自動アップグレードはメンテナンスウィンドウ内で実行されます。お客様のシステムに影響が出ないよう、適切なメンテナンスウィンドウを設定していることを確認してください。
2.  **GKEバージョンアップグレードへの備え**: Composerの基盤となるGKEがこれらの新しいバージョンにアップグレードされる可能性を考慮し、お客様のAirflowワークロードやカスタムコンポーネントが新しいGKEバージョンで問題なく動作するかを事前に検証する計画を立ててください。非推奨APIの使用状況も確認し、必要に応じて改修を検討してください。
用語説明:
*   **Stableチャネル (Stable Channel)**: GKEのリリースチャネルの一つで、最も安定性が重視されます。新機能の導入は
# Title: February 10, 2026 
Link: https://docs.cloud.google.com/release-notes#February_10_2026<br>
はい、Google Cloudのインフラエンジニアとして、Apigee Xに関するリリースノートの内容を調査し、影響分析を行いました。

---

# Apigee X

## Announcement
原文:
On February 10, 2026, we released an updated version of Apigee (1-17-0-apigee-2).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
Apigee X の新しいバージョン (1-17-0-apigee-2) が2026年2月10日にリリースされました。このリリースは現在 Google Cloud の全ゾーンで順次展開（ロールアウト）されており、完了には4営業日以上かかる可能性があります。ロールアウトが完了するまで、お客様の Apigee インスタンスでは新しい機能や修正が利用できない場合があります。

影響有無：
**影響：あり（ポジティブな影響）**
このアップデートは、Apigee X の新機能の導入、パフォーマンス改善、セキュリティ修正、バグ修正を含むため、全体的なサービス品質と安定性が向上します。しかし、ロールアウト期間中は、まだアップデートが適用されていないインスタンスと適用済みのインスタンスが混在する可能性があるため、特定の修正や機能に依存するアプリケーションでは、適用状況に注意が必要です。Google Cloud Composerとは直接的な影響はありません。

対処方法：
特別なユーザー操作は不要です。Apigee Xはマネージドサービスのため、Google Cloud側で自動的にアップデートが適用されます。
*   ロールアウト状況を把握し、Apigee インスタンスの挙動に変化がないか監視してください。
*   特に既存の機能を利用している場合、ロールアウト完了後に予期せぬ動作変更がないか、簡単な煙テスト（Smoke Test）やヘルスチェックを実施することをお勧めします。
*   今回のアップデートによる新機能の利用を計画している場合は、ロールアウト完了後に利用可能となることを考慮に入れてください。

用語説明：
*   **Apigee X**: API を管理、保護、分析するための Google Cloud のマネージドサービス。API プロキシの作成、デプロイ、トラフィックの管理、セキュリティポリシーの適用などを行います。
*   **ロールアウト (Rollout)**: ソフトウェアやサービスの新しいバージョンを段階的に本番環境に展開していくプロセス。これにより、リスクを最小限に抑えながら変更を適用できます。
*   **インスタンス (Instance)**: Apigee X 環境を構成する個々のコンポーネントまたは論理的な実行単位。

---

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **481735779, 457138941, 471232237** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:  - CVE-2025-61730- CVE-2025-68156- CVE-2025-54388- CVE-2025-61727- CVE-2025-61729 |
| **470375542** | Fix a memory leak which could result in a spike in 503 responses with "no_healthy_upstream" messages. |
| **480997525** | Fix for proxy calls failing with "The URI contains illegal characters" error after Netty upgrade. |
This addresses the following vulnerabilities: - CVE-2025-61730- CVE-2025-68156- CVE-2025-54388- CVE-2025-61727- CVE-2025-61729

[CVE-2025-61730](https://nvd.nist.gov/vuln/detail/CVE-2025-61730)
[CVE-2025-68156](https://nvd.nist.gov/vuln/detail/CVE-2025-68156)
[CVE-2025-54388](https://nvd.nist.gov/vuln/detail/CVE-2025-54388)
[CVE-2025-61727](https://nvd.nist.gov/vuln/detail/CVE-2025-61727)
[CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)

説明：
Apigee X のセキュリティおよび安定性に関する修正が含まれています。
*   Apigee のインフラストラクチャにおける複数の脆弱性 (CVE-2025-61730, CVE-2025-68156, CVE-2025-54388, CVE-2025-61727, CVE-2025-61729) が修正されました。これらの脆弱性に対処することで、サービスのセキュリティ体制が強化されます。
*   メモリリークが修正されました。この問題は、"no_healthy_upstream" メッセージを伴う 503 エラー応答の急増を引き起こす可能性がありました。
*   Netty のアップグレード後に発生していた "The URI contains illegal characters" エラーによるプロキシ呼び出しの失敗が修正されました。

影響有無：
**影響：あり（ポジティブな影響）**
Apigee X の運用セキュリティと安定性が大幅に向上します。
*   **セキュリティ**: 既知の脆弱性が修正されるため、潜在的な攻撃リスクが軽減されます。これは、API を公開しているサービスにとって非常に重要です。
*   **パフォーマンス・安定性**: メモリリークの修正により、503エラーの発生頻度が減少する可能性があり、サービスのアベイラビリティと信頼性が向上します。
*   **機能**: 特定の条件で発生していたプロキシ呼び出しエラーが解消され、API リクエストの処理がより安定します。
Google Cloud Composerとは直接的な影響はありません。

対処方法：
特別なユーザー操作は不要です。これらの修正は Apigee X のマネージドインフラストラクチャに自動的に適用されます。
*   Apigee X の API トラフィックやエラーレート（特に503エラー）に関する監視を継続し、修正が適用されたことによる安定性の改善を確認してください。
*   API のセキュリティスキャンや脆弱性診断を行っている場合は、今回の修正によりスキャン結果が改善されるか確認してください。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: 一般に公開されている情報セキュリティの脆弱性および露呈に関する識別子と情報を含むリスト。各CVE IDは特定の脆弱性を一意に識別します。
*   **メモリリーク (Memory Leak)**: プログラムが確保したメモリを解放し忘れ、結果的に利用可能なメモリが徐々に減少し、システムのパフォーマンス低下やクラッシュを引き起こす問題。
*   **503 Service Unavailable**: HTTP ステータスコードの一つで、サーバーが一時的にリクエストを処理できないことを示します。原因としては過負荷、メンテナンス、または「upstream」サーバーの問題などが考えられます。
*   **no_healthy_upstream**: ロードバランサーやプロキシが、トラフィックを転送すべき健全なバックエンド（upstream）サーバーを見つけられない場合に発生するエラーメッセージ。
*   **Netty**: 高性能なネットワークアプリケーション（クライアントとサーバー）を迅速に開発するための非同期イベント駆動型ネットワークアプリケーションフレームワーク。
*   **プロキシ (Proxy)**: クライアントからのリクエストを別のサーバー（ここでは Apigee X が管理するバックエンドAPI）に転送し、そのレスポンスをクライアントに返す仲介サーバー。
# Title: February 09, 2026 
Link: https://docs.cloud.google.com/release-notes#February_09_2026<br>
Google Cloudのインフラエンジニアとして、リリースノートに基づく影響調査を行いました。以下に製品ごとの回答をいたします。

---

# AlloyDB for PostgreSQL
## Fixed
原文: We are announcing the release of support for the AlloyDB language connectors and Auth Proxy with Auto IAM Authentication and managed connection pooling. This feature and the fix for the issue from below is available starting with maintenance version 20260107.02_05. Clusters with a maintenance window that may not have received this release can use self-service maintenance to perform a maintenance update.

[Auto IAM Authentication](https://docs.cloud.google.com/alloydb/docs/connect-iam#automatic)
[self-service maintenance](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance)

説明：
AlloyDB for PostgreSQLにおいて、AlloyDB言語コネクタ、Auth Proxy、自動IAM認証、およびマネージド接続プールのサポートがリリースされました。これらの新機能と、リリースノートに明記されていないものの何らかの問題に対する修正が、メンテナンスバージョン `20260107.02_05` から利用可能です。まだこのリリースが適用されていないクラスターについては、自己サービスメンテナンス機能を使用して手動でメンテナンスアップデートを実行できます。

影響有無：
**影響なし（ポジティブな機能追加と修正）**
このリリースは、既存の機能への破壊的な変更ではなく、新しい機能の追加と、それに付随する（または独立した）修正が主です。現在これらの機能を使用していない場合、既存のAlloyDB構成に直接的な悪影響はありません。ただし、新しい機能は運用の効率化やセキュリティ強化に寄与するため、利用を検討する価値があります。含まれる修正は、サービスの安定性や信頼性を向上させる可能性があります。

対処方法：
1.  **即座の対処は不要**: 現在、AlloyDB言語コネクタ、Auth Proxy、自動IAM認証、マネージド接続プールを使用していない場合、直ちに対応する必要はありません。
2.  **機能利用の検討**: これらの新しい機能（特に自動IAM認証やマネージド接続プール）の利用を検討する場合は、公式ドキュメントを参照し、必要に応じてAlloyDBクラスターをメンテナンスバージョン `20260107.02_05` 以降に更新してください。
3.  **計画的なアップデートの実施**: クラスターがまだこのバージョンに更新されていない場合、サービスの安定性やセキュリティ向上のため、メンテナンスウィンドウを利用した自動アップデートを待つか、または「自己サービスメンテナンス」機能を利用して計画的にアップデートを適用することを推奨します。

用語説明：
*   **AlloyDB for PostgreSQL**: Google Cloudが提供するフルマネージドのPostgreSQL互換データベースサービスです。ハイパフォーマンス、高可用性、スケーラビリティが特徴です。
*   **Language Connectors**: データベースが外部のプログラミング言語やランタイムと連携するための仕組みです。AlloyDBでは、例えばJavaScriptなどの言語でデータベース内のカスタムロジックを記述・実行できるようになります。
*   **Auth Proxy**: 認証プロキシの略で、アプリケーションとデータベース間の認証プロセスを仲介するコンポーネントです。これにより、認証情報の管理が簡素化され、セキュリティが向上します。
*   **Auto IAM Authentication**: Google Cloud IAM (Identity and Access Management) を用いて、ユーザーやサービスアカウントの認証情報でデータベースへ安全に接続できるようにする機能です。データベースのユーザー名・パスワード管理を不要にし、IAMポリシーに基づいたきめ細やかなアクセス制御を可能にします。
*   **Managed Connection Pooling**: データベースへの接続を効率的に管理する機能です。アプリケーションが接続するたびに新しい接続を確立するのではなく、既存の接続を再利用することで、データベースのリソース負荷を軽減し、アプリケーションのパフォーマンスを向上させます。
*   **Self-service maintenance**: ユーザーが任意のタイミングでGoogle Cloudサービスに対するメンテナンスアップデートを手動で実行できる機能です。自動メンテナンスウィンドウ以外で、計画的にアップデートを適用したい場合に便利です。

---

# Cloud Service Mesh
## Announcement
原文: The following images are now rolling out for managed Cloud Service Mesh:
- 1.21.6-asm.10 is rolling out to the rapid release channel.
- 1.20.8-asm.63 is rolling out to the regular release channel.
- 1.19.10-asm.57 is rolling out to the stable release channel.
These patch releases contain the fixes for the following managed Cloud Service Mesh CVEs:
| CVE | Proxy | Control Plane | CNI | Distroless | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2025-61729 | Yes | Yes | - | Yes | High (7.5) |
| CVE-2025-61727 | Yes | Yes | - | Yes | Medium (6.5) |
| CVE-2024-41996 | Yes | Yes | - | Yes | High (7.5) |
| CVE-2025-9086 | Yes | Yes | - | Yes | High (7.5) |
| CVE-2021-46848 | Yes | Yes | - | Yes | Critical (9.1) |
| CVE-2025-13151 | Yes | Yes | - | Yes | High (7.5) |
| CVE-2025-68973 | Yes | Yes | - | Yes | High (7.8) |
[CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)
[CVE-2025-61727](https://pkg.go.dev/vuln/GO-2025-4175)
[CVE-2024-41996](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-41996)
[CVE-2025-9086](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-9086)
[CVE-2021-46848](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2021-46848)
[CVE-2025-13151](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-13151)
[CVE-2025-68973](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-68973)

説明：
マネージドCloud Service Mesh (ASM) 向けに、新しいパッチリリースイメージが各リリースチャネル（rapid, regular, stable）に順次展開されていることがアナウンスされました。これらのパッチリリースには、複数の共通脆弱性識別子（CVE）に対するセキュリティ修正が含まれています。特に、深刻度Critical (9.1) の `CVE-2021-46848` を含む、多数のHighレベルの脆弱性が修正されています。修正対象コンポーネントは、プロキシ、コントロールプレーン、およびDistrolessイメージにわたります。

影響有無：
**ポジティブなセキュリティ強化**
このリリースは、既存のCloud Service Mesh環境のセキュリティ体制を大幅に強化するものです。特に、CriticalおよびHighレベルの複数のCVEが修正されているため、サービスのセキュリティリスクが低減します。マネージドCloud Service Meshを利用している場合、これらのアップデートはGoogle Cloudによって自動的に適用されるため、ユーザー側での破壊的変更は通常発生しません。機能やパフォーマンスに直接的な悪影響は想定されず、むしろ安定性の向上が期待されます。

対処方法：
1.  **自動適用と監視**: マネージドCloud Service Meshをご利用の場合、これらのイメージはGoogle Cloudによって自動的に展開されます。ユーザー側での直接的な操作は不要ですが、更新が正常に適用されたか、および適用後にサービスに予期せぬ影響がないかを監視することが推奨されます。
2.  **バージョンの確認**: ご自身の環境で利用しているCloud Service Meshのバージョンが更新されていることを確認してください。
3.  **セキュリティ体制の強化**: 複数の深刻な脆弱性（特に `CVE-2021-46848`）が修正されるため、速やかに最新のイメージが適用されることで、セキュリティリスクが最小化されます。

用語説明：
*   **Cloud Service Mesh (ASM)**: Google Cloudが提供する、Istioベースのフルマネージドサービスメッシュプラットフォームです。マイクロサービス間のトラフィック管理、セキュリティ、および可観測性を向上させます。
*   **Managed Cloud Service Mesh**: Cloud Service Meshのマネージド版であり、サービスメッシュのコントロールプレーンの運用と管理がGoogle Cloudによって行われます。これにより、ユーザーはアプリケーションのデプロイとデータプレーン（Envoyプロキシ）の管理に注力できます。
*   **Release Channel (Rapid, Regular, Stable)**: Google CloudやIstio/ASMなどのプロダクトで用いられるリリースサイクルです。
    *   **Rapid (高速チャネル)**: 最新の機能や修正が最も早く提供されるチャネル。
    *   **Regular (標準チャネル)**: ある程度のテストを経てリリースされる、バランスの取れたチャネル。
    *   **Stable (安定チャネル)**: 長期間のテストと検証が行われ、最も安定性が高いと判断されたバージョンが提供されるチャネルで、本番環境での利用が推奨されます。
*   **CVE (Common Vulnerabilities and Exposures)**: 共通脆弱性識別子。情報セキュリティの脆弱性に一意のIDを付与し、脆弱性情報を共有するための国際的な標準です。深刻度はCVSS (Common Vulnerability Scoring System) スコアで評価され、Critical (9.0-10.0), High (7.0-8.9), Medium (4.0-6.9), Low (0.1-3.9) の4段階に分類されます。
*   **Proxy**: サービスメッシュにおいて、各サービス（Pod）のサイドカーとしてデプロイされるEnvoyプロキシなどのことです。サービス間の通信をインターセプトし、ルーティング、ポリシー適用、テレメトリ収集などを行います。
*   **Control Plane**: サービスメッシュ全体の管理機能を担うコンポーネント群です。Istioでは`istiod`として提供され、データプレーン（Proxy）の設定やポリシーを一元的に制御します。
*   **Distroless**: 最小限のランタイム依存関係しか含まない軽量なDockerイメージのことです。不要なコンポーネントを含まないため、攻撃対象領域が削減され、セキュリティが強化されます。