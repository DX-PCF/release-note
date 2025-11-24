
# Title: November 21, 2025 
Link: https://docs.cloud.google.com/release-notes#November_21_2025<br>
はい、承知いたしました。Google Cloudのインフラエンジニアとして、ご提示いただいたリリースノートについて、製品ごとの影響有無と対処方法を専門的な言葉遣いと書式でご説明します。

---

# Apigee X

## Issue
原文: `Message Processor returns 500 error with "Duplicate Header "authorization"". When multiple authorization headers are present in a request, the Apigee ingress gateway doesn't concatenate them into a single header. This results in the Message Processor returning a 500 error with a "Duplicate Header "authorization"" message. For more information, see Apigee known issues. [Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues)`

説明：
Apigee XのIngress Gatewayにおいて、受信したHTTPリクエストに複数の`Authorization`ヘッダーが含まれる場合、それらを単一のヘッダーとして連結処理せず、その結果、Message Processorが`"Duplicate Header "authorization""`というエラーメッセージと共に`HTTP 500 Internal Server Error`を返却する既知の問題です。この事象は、RFC 7230において複数ヘッダーフィールドの取り扱いが定義されているものの、Apigee Ingress Gatewayが特定の条件下でこの仕様に適合しない挙動を示すことを示唆しています。

影響有無：
当環境がApigee Xを利用しており、かつ、クライアントからのAPIリクエストにおいて、意図せずまたは意図的に複数の`Authorization`ヘッダー（例: `Authorization: Bearer token1`, `Authorization: Bearer token2`のような形式）が送出される可能性がある場合、この問題の影響を受け、APIコールが`500`エラーで失敗する可能性があります。これはAPIの可用性に直接影響を及ぼす事象です。

対処方法：
1.  **クライアント側での対応**: 最も直接的な対処法として、APIを呼び出すクライアントアプリケーション側で、リクエストに単一の`Authorization`ヘッダーのみが含まれるように修正を適用することを推奨します。
2.  **Apigee Known Issuesの監視**: 現時点ではApigee X側のパッチリリースに関する情報がないため、[Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues) ドキュメントを定期的に監視し、この問題に対する公式な修正や回避策が提供され次第、速やかに適用を検討します。
3.  **（暫定的な回避策の検討）**: Apigeeプロキシフロー内でJavaScriptポリシーやExtract Variablesポリシー等を用いて、Authorizationヘッダーを正規化するカスタムロジックの実装を検討することも可能ですが、これはあくまで暫定的な回避策であり、パフォーマンスへの影響や複雑性の増加を考慮する必要があります。

用語説明：
*   **Apigee X**: Google Cloudが提供するフルマネージドのAPI管理プラットフォーム。APIの設計、デプロイ、セキュリティ、監視、分析機能を提供します。
*   **Ingress Gateway**: 外部からのAPIリクエストをApigeeのAPIプロキシにルーティングする、トラフィックの入口となるコンポーネントです。
*   **Message Processor**: Apigeeのランタイムコンポーネントであり、APIプロキシのリクエストおよびレスポンスの処理ロジックを実行する役割を担います。
*   **`Authorization` ヘッダー**: HTTPリクエストにおいて、クライアントがサーバーに対して認証情報（例: OAuth 2.0トークン、Basic認証クレデンシャル）を提示するために使用される標準的なHTTPヘッダーです。

---

# Google Kubernetes Engine

## Issue
原文: `GKE versions earlier than 1.32 don't support direct NFS volume mounts to NFS volumes that exclusively use an NFS protocol greater than NFSv4.0. When using direct NFS volume mounts, Pods on GKE node versions earlier than 1.32 might fail to mount NFS volumes that are configured to only support protocols greater than NFSv4.0 (such as NFSv4.1 or NFSv4.2). This issue occurs because the containerized_mounter on these earlier GKE versions uses version 1.2.8 of the nfs-utils package, which doesn't support NFSv4 minor versions. As a result, the mount process fails with the mount.nfs: access denied by server error message. This issue doesn't affect GKE version 1.32 and later, which include an updated version of the nfs-utils package. To resolve this issue, try one of the following options: - Upgrade clusters to GKE version 1.32 or later. - Configure the NFS volume to support both the NFSv3 and NFSv4 protocols, which allows the mount to succeed by falling back to a compatible version. - Use a PersistentVolume and PersistentVolumeClaim to mount the NFS volume, which allows for explicit NFS version specification.`

説明：
GKEバージョン1.32より前のノードイメージにおいて、NFSv4.0を超えるNFSプロトコルバージョン（例: NFSv4.1、NFSv4.2）を排他的に利用するNFSボリュームに対する直接マウント（`direct NFS volume mounts`）がサポートされていない問題です。この原因は、該当するGKEバージョンで使用されている`containerized_mounter`が、NFSv4のマイナーバージョンを正しく扱えない`nfs-utils`パッケージのバージョン1.2.8に依存しているためです。この結果、マウントプロセスが`mount.nfs: access denied by server`エラーで失敗する可能性があります。この問題は、`nfs-utils`パッケージが更新されたGKEバージョン1.32以降では解消されています。

影響有無：
当環境において、Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) はGKE上に構築されますが、通常、Composerは永続ストレージとしてCloud Storage FUSEを利用し、直接NFSボリュームをPodにマウントするケースは稀です。
ただし、以下のいずれかの条件に該当する場合、この問題の影響を受ける可能性があります。
*   GKEクラスターのバージョンが1.32より前である。
*   ワークロードでNFSv4.1またはNFSv4.2を排他的に利用するNFSサーバーをPodが直接マウントしている。

対処方法：
上記の条件に該当する場合、以下のいずれかの方法で問題を解消してください。
1.  **GKEクラスターのアップグレード**: GKEクラスターをバージョン1.32以降にアップグレードすることを強く推奨します。これにより、更新された`nfs-utils`パッケージが適用され、問題が解決されます。
2.  **NFSボリュームのプロトコル設定変更**: NFSサーバーの構成を変更し、NFSv3とNFSv4の両プロトコルをサポートするように設定します。これにより、互換性のあるバージョンにフォールバックしてマウントが成功する可能性があります。
3.  **PersistentVolume (PV) および PersistentVolumeClaim (PVC) の利用**: Kubernetesの標準的なストレージ抽象化であるPV/PVCを用いてNFSボリュームをマウントします。この方法では、NFSバージョンを明示的に指定できるため、問題の回避が可能です。

用語説明：
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するフルマネージドのKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、スケーリング、管理を容易にします。
*   **NFS (Network File System)**: ネットワークを介してファイルシステムを共有するための分散ファイルシステムプロトコル。
*   **NFSv4.0, NFSv4.1, NFSv4.2**: NFSプロトコルのバージョン。NFSv4は以前のバージョンに比べてステートフルなプロトコルであり、セキュリティやパフォーマンスが向上しています。
*   **`containerized_mounter`**: GKEノード上で実行されるコンポーネントで、Kubernetesボリュームのマウント処理をコンテナ内で実行するために使用されます。
*   **`nfs-utils`**: NFSクライアントおよびサーバーのユーティリティを提供するLinuxパッケージ。NFSマウントコマンド（`mount.nfs`）などが含まれます。
*   **PersistentVolume (PV)**: クラスター管理者によってプロビジョニングされたストレージのネットワークストレージ。Kubernetesクラスターにおけるストレージリソースの抽象化です。
*   **PersistentVolumeClaim (PVC)**: ユーザーによるストレージのリクエスト。Podがストレージリソースを要求する際に使用します。

## Issue
原文: `In GKE versions 1.34.1-gke.2037001 and 1.34.1-gke.2541000, Arm nodes that use an Ubuntu node image might incorrectly use an image with a 64 KB page size instead of the default 4 KB page size. Avoid using version 1.34.1-gke.2037001 and 1.34.1-gke.2541000 for your Ubuntu Arm nodes.`

説明：
GKEバージョン`1.34.1-gke.2037001`および`1.34.1-gke.2541000`において、Ubuntuノードイメージを使用するArmアーキテクチャのGKEノードが、デフォルトの4KBページサイズではなく、誤って64KBページサイズのOSイメージで起動してしまう可能性がある問題です。この特定のバージョンの利用は、UbuntuベースのArmノードにおいては推奨されません。誤ったページサイズの使用は、アプリケーションのパフォーマンス特性や互換性に予期せぬ影響を与える可能性があります。

影響有無：
当環境でGKEクラスターのノードプールにArmアーキテクチャのノードを使用しており、かつノードイメージとしてUbuntuを選択している場合、指定された影響を受けるGKEバージョン（`1.34.1-gke.2037001`または`1.34.1-gke.2541000`）を使用している場合にこの問題の影響を受けます。
Google Cloud Composerは通常、x86アーキテクチャのノードを使用するため、直接的な影響は低いと想定されます。しかし、Armベースのカスタムノードプールを構築している場合は、この問題に注意が必要です。

対処方法：
1.  **対象バージョンの使用回避**: ArmアーキテクチャかつUbuntuノードイメージを使用するGKEノードにおいては、GKEバージョン`1.34.1-gke.2037001`および`1.34.1-gke.2541000`の使用を避けてください。
2.  **アップグレードまたはダウングレード**: 既にこれらのバージョンを使用している場合は、直ちに影響のない最新の安定バージョン（例: 最新のパッチバージョンや次のマイナーバージョン）にアップグレードするか、問題の発生しない以前の安定バージョンにダウングレードすることを推奨します。
3.  **ノードイメージの検討**: 必要に応じて、Ubuntu以外のノードイメージ（例: Container Optimized OS (COS)）の使用を検討してください。COSはGoogleがGKE用に最適化したイメージであり、安定性とセキュリティが高いとされています。

用語説明：
*   **Armノード**: ARMアーキテクチャのプロセッサを搭載したGKEノード。特定のワークロードにおいて、x86ベースのノードに比べて優れたコスト効率やエネルギー効率を提供する場合があります。
*   **Ubuntuノードイメージ**: GKEノードで使用可能なオペレーティングシステムイメージの一つで、広く利用されているLinuxディストリビューションであるUbuntuをベースにしています。
*   **ページサイズ (Page Size)**: オペレーティングシステムが仮想メモリを管理する際の最小単位。CPUとメモリ間のデータ転送の粒度を決定し、アプリケーションのメモリアクセス性能やシステムリソースの利用効率に影響を与える可能性があります。一般的なLinuxシステムでは4KBがデフォルトですが、一部のハードウェアや特定の用途ではより大きなページサイズ（例: 64KB、2MB、1GB）が使用されることがあります。
*   **Container Optimized OS (COS)**: GoogleがKubernetesワークロード向けに最適化した、セキュリティと安定性に重点を置いた最小限のLinuxディストリビューション。GKEのデフォルトノードイメージとしてよく利用されます。
# Title: November 20, 2025 
Link: https://docs.cloud.google.com/release-notes#November_20_2025<br>
# Google Kubernetes Engine
## Changed
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
説明：Google Kubernetes Engine (GKE) クラスタの新しいバージョンが、新規クラスタの作成および既存クラスタのコントロールプレーンとノードの手動アップグレード