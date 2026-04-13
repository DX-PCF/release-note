
# Title: April 09, 2026 
Link: https://docs.cloud.google.com/release-notes#April_09_2026<br>
Google Cloud のリリースノートに基づき、構築済みのサービスへの影響を調査し、以下の通りご報告いたします。

---

# Apigee X

## Change

原文: Relaxed limitation on header name for Client IP resolution. The client IP can now be resolved from any header, not just the `X-Forwarded-For` header. The most common headers are `X-Forwarded-For` or `True-Client-Ip`. For more information, see [Client IP resolution](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution).

説明: Apigee がクライアントの IP アドレスを特定する際に、これまでは主に `X-Forwarded-For` ヘッダーに限定されていましたが、今回の変更により任意のHTTPヘッダーから IP アドレスを解決できるようになりました。これにより、`True-Client-Ip` などの他の一般的なヘッダーも利用して、より柔軟なクライアントIPの解決が可能となります。

影響有無: 影響なし。
これは既存機能の動作を変更するものではなく、機能拡張（追加）にあたります。現在 `X-Forwarded-For` ヘッダーを利用してクライアントIPを解決している場合、既存の構成に影響はありません。より柔軟なIP解決が必要な場合に、新しい設定オプションを利用できるようになります。

対処方法: 特段の対応は不要です。
もし、現在 `X-Forwarded-For` 以外のヘッダーからクライアントIPを解決する要件があり、Apigee でそのIPアドレス情報を利用したい場合は、Apigee の Client IP resolution 設定を見直すことで、この新しい機能を利用できます。

用語説明:
*   **`X-Forwarded-For` (XFF)**: HTTP ヘッダーの一種で、HTTP プロキシやロードバランサを経由して Web サーバーにリクエストが届いた際に、クライアントのオリジナル IP アドレスを識別するために広く使用されます。
*   **`True-Client-Ip`**: Cloudflare など、一部の Content Delivery Network (CDN) やプロキシサービスが、リクエスト元のクライアントのオリジナル IP アドレスを伝えるために使用するカスタム HTTP ヘッダーです。
*   **Client IP resolution**: Apigee が受信した API リクエストから、元のクライアントの IP アドレスを特定するプロセスです。これにより、IP アドレスに基づくセキュリティポリシーの適用、アクセス制御、ログ記録などが可能になります。

---

# Google Kubernetes Engine (GKE)

## Change

原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE cluster upgrades](https://cloud.cloud.google.com/kubernetes-engine/upgrades).

説明: GKE クラスターの新しいバージョンがリリースされ、新規クラスターの作成、および既存クラスターのコントロールプレーンとノードのアップグレードで利用可能になりました。これにより、最新の機能、バグ修正、パフォーマンス改善が提供されます。

影響有無: 影響あり（ポジティブな影響）。
直接的な機能変更や非互換性の発生はありませんが、利用可能な GKE バージョンが増えることで、クラスターの安定性、セキュリティ、およびパフォーマンスの向上が期待されます。
*   **オートアップグレードが有効な場合**: クラスターは自動的にこれらの新しいバージョンにアップグレードされる可能性があります。これにより、運用負担なく最新の状態を維持できます。
*   **手動アップグレードの場合**: 新しいバージョンへの計画的なアップグレードが可能になります。

対処方法:
*   GKE クラスターでオートアップグレードが有効になっている場合、特別な対応は不要です。GKE は設定されたメンテナンスウィンドウ内で自動的にアップグレードを実行します。アップグレードの進行状況は GKE コンソールまたは `gcloud container operations list` コマンドで確認できます。
*   手動でアップグレードを管理している場合、これらの新しいバージョンへの計画的なアップグレードを検討してください。アップグレード前には、テスト環境でのアプリケーションの互換性確認を強く推奨します。
*   Google Cloud Composer はマネージドサービスであり、基盤となる GKE のバージョンは Google Cloud Composer 側のリリースサイクルで管理されます。そのため、今回の GKE バージョンアップが直ちに Composer 環境の GKE バージョンに影響を与えることはありません。

## Security

原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. (Details on specific GKE and COS versions follow in original text)

説明: 今回の GKE リリースでは、更新された Container-Optimized OS (COS) イメージを使用する新しい GKE バージョンが含まれています。これらの COS イメージには、前回の GKE リリース以降に公開されたすべてのセキュリティ修正が累積的に適用されています。これにより、GKE ノードの基盤となる OS のセキュリティが強化されます。

影響有無: 影響あり（ポジティブな影響）。
GKE ノードの OS イメージが更新されることで、既知の脆弱性が修正され、クラスター全体のセキュリティ体制が向上します。これはシステムをより堅牢にするための重要な更新です。

対処方法:
*   GKE クラスターのオートアップグレードが有効になっている場合、ノードも自動的に更新され、セキュリティ修正が適用されます。特別な対応は不要です。
*   手動でノードのアップグレードを管理している場合、セキュリティリスクを最小限に抑えるため、これらの新しい GKE バージョンへの速やかなアップグレードを検討してください。
*   Google Cloud Composer はマネージドサービスであるため、Composer 環境のノード OS アップデートは Google Cloud Composer サービス側で管理されます。現在の Composer バージョン 2.7.1 がこれらの COS バージョンを使用するかは、Composer のリリースノートで確認する必要がありますが、一般的には、セキュリティ修正はサービス提供者側で適宜適用されます。

用語説明:
*   **Container-Optimized OS (COS)**: Google Compute Engine で利用できる、コンテナ実行に特化し、セキュリティと信頼性を最大化するように最適化された Linux ベースのオペレーティングシステムです。GKE クラスターのノード (ワーカーノード) の基盤 OS として使用されます。
*   **セキュリティ修正**: ソフトウェアやオペレーティングシステムに発見された脆弱性（セキュリティ上の欠陥）を修復するためのパッチやアップデート。

## Change

原文: The following versions are now available in the Stable channel: (versions listed) / Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: (versions listed)

説明: GKE の Stable リリースチャネルにおいて、新たに複数のバージョンが利用可能になりました。このチャネルに属するクラスターは、これらの新しいバージョンをオートアップグレードのターゲットとして認識し、コントロールプレーンおよびノードが自動的に更新される可能性があります。

影響有無: 影響あり。
*   **GKE クラスターを利用している場合**: 現在利用している GKE クラスターが Stable チャネルに登録されており、かつオートアップグレードが有効な場合、これらの新しいバージョンへの自動アップグレードがスケジュールされる可能性があります。これにより、クラスターが最新の状態に保たれます。
*   **Google Cloud Composer**: 前述の通り、Composer の基盤となる GKE バージョンは Composer のリリースサイクルに依存します。現在の Composer 2.7.1 が直ちにこれらの GKE バージョンにアップグレードされることはありませんが、将来の Composer アップデートでこれらの GKE バージョンが採用される可能性があります。

対処方法:
*   GKE クラスターのオートアップグレードが有効になっている場合、特に対応は不要です。アップグレードのスケジュールや進捗を監視し、予期せぬ問題が発生しないか確認してください。
*   アップグレードは設定されたメンテナンスウィンドウに従って実行されます。メンテナンスウィンドウやメンテナンス除外期間の設定を確認し、必要に応じて調整してください。

## Change

原文: The following versions are now available in the Regular channel: (versions listed)

説明: GKE の Regular リリースチャネルにおいて、新たに複数のバージョンが利用可能になりました。このチャネルに属するクラスターは、これらの新しいバージョンをオートアップグレードのターゲットとして認識し、コントロールプレーンおよびノードが自動的に更新される可能性があります。

影響有無: 影響あり。
*   **GKE クラスターを利用している場合**: 現在利用している GKE クラスターが Regular チャネルに登録されており、かつオートアップグレードが有効な場合、これらの新しいバージョンへの自動アップグレードがスケジュールされる可能性があります。
*   **Google Cloud Composer**: 同様に、Composer の基盤 GKE バージョンは Composer のリリースサイクルに依存します。直ちに Composer 環境に影響はありません。

対処方法:
*   GKE クラスターのオートアップグレードが有効になっている場合、特に対応は不要です。アップグレードのスケジュールや進捗を監視し、必要に応じてメンテナンスウィンドウなどを調整してください。

## Change

原文: The following versions are now available in the Rapid channel: (versions listed)

説明: GKE の Rapid リリースチャネルにおいて、新たに複数のバージョンが利用可能になりました。このチャネルに属するクラスターは、これらの新しいバージョンをオートアップグレードのターゲットとして認識し、コントロールプレーンおよびノードが自動的に更新される可能性があります。

影響有無: 影響あり。
*   **GKE クラスターを利用している場合**: 現在利用している GKE クラスターが Rapid チャネルに登録されており、かつオートアップグレードが有効な場合、これらの新しいバージョンへの自動アップグレードがスケジュールされる可能性があります。
*   **Google Cloud Composer**: 同様に、Composer の基盤 GKE バージョンは Composer のリリースサイクルに依存します。直ちに Composer 環境に影響はありません。

対処方法:
*   GKE クラスターのオートアップグレードが有効になっている場合、特に対応は不要です。Rapid チャネルは最も迅速に新バージョンが提供されるため、頻繁なアップグレードが行われる可能性があります。アプリケーションの互換性テストを継続的に実施することが推奨されます。

## Change

原文: The following versions are now available: (control plane versions listed) The following node versions are now available: (node versions listed)

説明: 新しいGKEのコントロールプレーンバージョンおよびノードバージョンが利用可能になりました。これらのバージョンは、新規クラスターの作成や既存クラスターのアップグレード時に選択できます。

影響有無: 影響あり（ポジティブな影響）。
GKE クラスターを利用している場合、より新しい安定したバージョンを選択できるようになります。これは、セキュリティ、機能、パフォーマンスの面で改善をもたらします。

対処方法:
*   GKE クラスターのアップグレードを計画する際に、これらの新しいバージョンの中から適切なものを選択できます。
*   新規クラスターをデプロイする際にも、これらの新しいバージョンを選択して、最新の環境を構築できます。
*   Google Cloud Composer のユーザーとしては、直接の対処は不要です。

## Change

原文: The following versions are now available in the Extended channel: (versions listed)

説明: GKE の Extended リリースチャネルにおいて、新たに複数のバージョンが利用可能になりました。このチャネルは特定のマイナーバージョンを長期にわたってサポートするためのもので、Stability が最も重視されます。

影響有無: 影響あり。
*   **GKE クラスターを利用している場合**: 現在利用している GKE クラスターが Extended チャネルに登録されており、かつオートアップグレードが有効な場合、これらの新しいバージョンへの自動アップグレードがスケジュールされる可能性があります。Extended チャネルは、サポート期間が長い特定のマイナーバージョンを維持したい場合に選択されます。
*   **Google Cloud Composer**: 同様に、Composer の基盤 GKE バージョンは Composer のリリースサイクルに依存します。直ちに Composer 環境に影響はありません。

対処方法:
*   GKE クラスターのオートアップグレードが有効になっている場合、特に対応は不要です。このチャネルは安定性を重視するため、他のチャネルに比べてアップグレードの頻度は低くなります。

用語説明（GKE共通）:
*   **GKE (Google Kubernetes Engine)**: Google Cloud が提供するマネージドな Kubernetes サービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **GKE リリースチャネル (Release Channels)**: GKE クラスターのアップグレードのタイミングと安定性を制御するための設定です。
    *   **Rapid (ラピッド)**: 最も早く新機能やアップデートが提供されますが、安定性については他のチャネルに劣る可能性があります。開発環境やテスト環境に適しています。
    *   **Regular (レギュラー)**: Rapid より遅れて新機能が提供され、より安定性が高いチャネルです。本番環境にも利用されることがあります。
    *   **Stable (ステーブル)**: 最も安定性が高く、新機能の提供は他のチャネルより遅れます。ミッションクリティカルな本番環境での利用に推奨されます。
    *   **Extended (エクステンデッド)**: 特定のマイナーバージョンを長期にわたってサポートすることを目的としたチャネルです。安定性と長期サポートが最優先される場合に選択されます。
*   **コントロールプレーン (Control Plane)**: Kubernetes クラスターの管理層であり、API サーバー、スケジューラー、コントローラーマネージャーなどが含まれます。クラスターの状態を管理し、リソースのデプロイやスケーリングを制御します。GKE では Google が管理します。
*   **ノード (Node)**: Kubernetes クラスター内で実際にコンテナ化されたアプリケーション（Pod）が実行される仮想マシンまたは物理マシンです。ワーカーノードとも呼ばれます。