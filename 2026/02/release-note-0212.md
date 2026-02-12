
# Title: February 10, 2026 
Link: https://docs.cloud.google.com/release-notes#February_10_2026<br>
Google Cloudのインフラエンジニアとして、Apigee Xのリリースノートについて調査結果を報告します。

---

# Apigee X

## Announcement

原文: On February 10, 2026, we released an updated version of Apigee (1-17-0-apigee-2).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
2026年2月10日にApigeeの新しいバージョン(1-17-0-apigee-2)がリリースされました。このリリースは本日より順次展開されており、すべてのGoogle Cloudゾーンへの適用には4営業日以上かかる場合があります。この展開が完了するまでは、ご利用のインスタンスで新しい機能や修正が利用できない可能性があります。

影響有無：
影響なし。
これは新しいバージョンがリリースされ、それが自動的にロールアウト中であるというアナウンスであり、ユーザー側で直ちに何か操作や設定変更が必要になるものではありません。Google Cloudが提供するマネージドサービスであるため、基盤の更新は自動的に適用されます。展開完了まで新機能や修正が利用できない可能性があるという点も、既存の機能の利用には影響しません。

対処方法：
特にユーザー側で必要な対処はありません。Google Cloudによる自動的な更新を待ってください。

用語説明：
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームで、APIの設計、デプロイ、セキュリティ、監視、分析などを一元的に行います。
*   **ロールアウト (Rollout)**: ソフトウェアやシステムの新しいバージョンや機能を、本番環境に段階的に展開していくプロセスを指します。

## Security

原文:
| Bug ID | Description |
| --- | --- |
| **481735779, 457138941, 471232237** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:  - CVE-2025-61730- CVE-2025-68156- CVE-2025-54388- CVE-2025-61727- CVE-2025-61729 |
| **470375542** | Fix a memory leak which could result in a spike in 503 responses with "no_healthy_upstream" messages. |
| **480997525** | Fix for proxy calls failing with "The URI contain illegal characters" error after Netty upgrade. |

説明：
Apigeeインフラストラクチャにおける複数のセキュリティ脆弱性（CVE-2025-61730、CVE-2025-68156、CVE-2025-54388、CVE-2025-61727、CVE-2025-61729）が修正されました。また、メモリリークにより「no_healthy_upstream」メッセージを伴う503エラーが増加する問題と、Nettyアップグレード後に「The URI contain illegal characters」エラーでプロキシ呼び出しが失敗する問題も修正されています。

影響有無：
間接的に影響あり（ポジティブな影響）。
これらの修正はApigeeのインフラストラクチャおよび安定性に関するものであり、ユーザー側で直接操作する必要はありませんが、サービス基盤のセキュリティと信頼性が向上します。特に、メモリリークやURI不正文字のエラーによるサービス中断や品質低下のリスクが軽減されます。

対処方法：
特にユーザー側で必要な対処はありません。Google Cloudによる自動的な更新を待ってください。もしこれらの問題（特に503エラーやURIエラー）に既存の環境で直面していた場合は、修正適用後に改善されるか監視を推奨します。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアの脆弱性に関する情報を識別するための、国際的に合意された命名規則です。各脆弱性には一意のCVE IDが割り当てられます。
*   **Apigee infrastructure (Apigeeインフラストラクチャ)**: Apigeeサービスを稼働させるための基盤となる、ハードウェア、ソフトウェア、ネットワークなどのIT要素を指します。Google Cloudが管理しています。
*   **メモリリーク (Memory Leak)**: プログラムが確保したメモリを解放し忘れ、使用可能なメモリが徐々に減少していく現象。システム全体のパフォーマンス低下やクラッシュにつながる可能性があります。
*   **503 Service Unavailable**: HTTPステータスコードの一つで、サーバーが一時的にリクエストを処理できない状態であることを示します。
*   **no_healthy_upstream**: Apigeeにおいて、APIゲートウェイがバックエンドサービスへの健全な接続を見つけられない場合に発生する可能性のあるエラーメッセージです。
*   **Netty**: 高性能なネットワークアプリケーション開発フレームワークで、ApigeeのようなAPIゲートウェイの内部で、HTTP/HTTPS通信などのネットワーク処理に使用されることがあります。
*   **URI (Uniform Resource Identifier)**: Web上のリソースを一意に識別するための文字列です。Webページのアドレスなどがこれに該当します。不正な文字が含まれると、リソースへのアクセスができないことがあります。
# Title: February 09, 2026 
Link: https://docs.cloud.google.com/release-notes#February_09_2026<br>
Google Cloudのインフラエンジニアとして、ご質問いただいたリリースノートについて、構築済みのサービスへの影響を調査し、以下の通り回答いたします。

---

# AlloyDB for PostgreSQL
## Fixed
**原文**:
We are announcing the release of support for the AlloyDB language connectors and Auth Proxy with Auto IAM Authentication and managed connection pooling. This feature and the fix for the issue from below is available starting with maintenance version 20260107.02_05. Clusters with a maintenance window that may not have received this release can use self-service maintenance to perform a maintenance update.

**説明**:
AlloyDB for PostgreSQLにおいて、以下の新機能がサポートされました。
*   AlloyDB言語コネクタのサポート
*   Auth Proxyにおける自動IAM認証 (Auto IAM Authentication)
*   マネージド接続プーリング

これらの機能追加と、関連する不具合の修正がメンテナンスバージョン `20260107.02_05` 以降で利用可能になります。もしお使いのAlloyDBクラスタがこのリリースを受けていない場合、セルフサービスメンテナンス機能を利用して手動でアップデートを適用することができます。

**影響有無**:
既存のAlloyDBクラスタのメンテナンスバージョンが `20260107.02_05` 未満である場合、このリリースに含まれる新機能や不具合修正はまだ適用されていません。
この変更は、既存の動作に非互換性のある変更をもたらすものではなく、機能追加と不具合修正です。そのため、既存のワークロードに対して直接的なマイナスの影響はありません。
新機能（例えば、アプリケーションでAlloyDB言語コネクタやAuto IAM Authenticationを利用したい場合）の利用、またはセキュリティと安定性向上のための不具合修正の適用を希望する場合は、影響があります。

**対処方法**:
1.  **現在のAlloyDBクラスタのメンテナンスバージョンを確認してください。**
2.  もしバージョンが `20260107.02_05` 未満で、これらの新機能の利用を検討している場合、または修正された不具合の影響を受けている可能性があり、早期に修正を適用したい場合は、計画的なメンテナンスウィンドウを設けてセルフサービスメンテナンスを利用し、クラスタをアップデートすることを推奨します。
    *   [セルフサービスメンテナンス](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance)
3.  定期メンテナンスウィンドウを設定している場合、次回のメンテナンス時に自動的にアップデートされる可能性もあります。

**用語説明**:
*   **AlloyDB for PostgreSQL**: Google Cloudが提供するフルマネージドなPostgreSQL互換のエンタープライズ向けデータベースサービスです。高性能、高可用性、スケーラビリティが特徴です。
*   **AlloyDB language connectors**: AlloyDBが外部のプログラミング言語（例: Python）で記述された関数やライブラリを直接データベース内で実行できるようにする機能です。これにより、AI/ML機能などとの連携が容易になります。
*   **Auth Proxy with Auto IAM Authentication**: AlloyDBへの接続を安全に行うためのプロキシです。特に「Auto IAM Authentication」機能は、Google Cloud IAM (Identity and Access Management) を利用してデータベースユーザーの認証を自動的に行い、データベースにパスワードを直接保存・管理する手間を省き、セキュリティを向上させます。
*   **Managed connection pooling**: データベースへの接続を効率的に管理し、再利用することで、アプリケーションからの接続オーバーヘッドを削減し、データベースのパフォーマンスとスケーラビリティを向上させる機能です。Google Cloudによって完全に管理されます。
*   **Maintenance version**: クラウドサービスが提供する、特定の機能セットやバグ修正を含むソフトウェアのバージョンです。

---

# Cloud Service Mesh
## Announcement
**原文**:
The following images are now rolling out for managed Cloud Service Mesh:
*   1.21.6-asm.10 is rolling out to the rapid release channel.
*   1.20.8-asm.63 is rolling out to the regular release channel.
*   1.19.10-asm.57 is rolling out to the stable release channel.

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

**説明**:
マネージドCloud Service Mesh向けに、各リリースチャネル（rapid, regular, stable）で新しいパッチリリースイメージが順次展開されています。これらのパッチリリースには、複数の重要なCVE（Common Vulnerabilities and Exposures）に対するセキュリティ修正が含まれており、中には深刻度「Critical (9.1)」や「High (7.5, 7.8)」の脆弱性も含まれています。

**影響有無**:
現在、マネージドCloud Service Meshをご利用の場合、これらのアップデートは各チャネルのポリシーに基づいて自動的に適用されます。したがって、お客様側での直接的な操作は不要です。
このアップデートはセキュリティ修正が主であるため、既存のワークロードに対する機能的な影響は極めて低いと考えられますが、セキュリティ体制は大幅に向上します。
Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3)は、内部的にはGKE上で動作しますが、直接Cloud Service Meshを利用する構成は一般的ではありません。もしComposer環境がCloud Service Meshを明示的に利用するよう構成されている場合（例: GKEクラスタがService Meshを有効化している場合）、セキュリティの向上という恩恵を受けます。

**対処方法**:
マネージドCloud Service Meshを利用している場合、アップデートは自動的に適用されるため、特別な対処は不要です。
セキュリティパッチが含まれるため、セキュリティの観点から推奨されるアップデートです。
アップデートが適用された後、既存のワークロードに予期せぬ影響がないか、サービスメッシュの監視（トラフィック、エラーレート、レイテンシなど）を継続することをお勧めします。

**用語説明**:
*   **Cloud Service Mesh**: Google Cloudが提供する、Istioベースのフルマネージドなサービスメッシュプラットフォームです。サービス間のトラフィック管理、セキュリティ、可観測性を提供します。
*   **Managed Cloud Service Mesh**: Cloud Service Meshのデプロイモデルの一つで、コントロールプレーンの運用と管理をGoogle Cloudが担当し、ユーザーはデータプレーンの管理に集中できます。
*   **Release Channel (Rapid/Regular/Stable)**: Google Cloudのサービス（GKEやCloud Service Meshなど）で、機能やアップデートのリリース速度と安定性レベルを選択するためのチャネルです。
    *   **Rapid**: 最新機能が最も早く提供されるが、安定性は他のチャネルより低い可能性があります。
    *   **Regular**: 安定性と新機能のバランスが取れています。
    *   **Stable**: 最も安定性が高く、新機能の導入は慎重に進められます。
*   **Patch Releases**: 主にバグ修正やセキュリティ脆弱性の修正を含む小規模なソフトウェアアップデートです。
*   **CVE (Common Vulnerabilities and Exposures)**: 一般に公開されている情報セキュリティ脆弱性とその識別子のリストです。`CVE-YYYY-NNNNN` の形式で一意に識別されます。
*   **Proxy**: サービスメッシュにおいて、各サービス（マイクロサービス）のサイドカーとしてデプロイされる軽量なプロキシ（例: Envoyプロキシ）です。サービス間のトラフィックルーティング、ポリシー適用、メトリクス収集などを担当します。
*   **Control Plane**: サービスメッシュの管理層であり、データプレーンのプロキシを設定・制御し、メッシュ全体のポリシー、ルーティング、セキュリティを管理します。
*   **CNI (Container Network Interface)**: コンテナのネットワーク設定を行うためのKubernetes標準インターフェースです。
*   **Distroless**: コンテナイメージのタイプの一つで、オペレーティングシステムのディストリビューションを含まず、アプリケーションの実行に必要な最小限の依存関係のみを持つイメージです。攻撃対象領域を減らし、イメージサイズを小さくする目的で使用されます。