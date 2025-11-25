
# Title: November 24, 2025 
Link: https://docs.cloud.google.com/release-notes#November_24_2025<br>
# Cloud Composer
## Issue
原文:
We discovered an issue that might impact the reporting of metrics in the
following recently released Cloud Composer versions:

- composer-2.15.4-airflow-*
- composer-3-airflow-2.10.5-build.20
- composer-3-airflow-2.9.3-build.40
- composer-3-airflow-3.1.0-build.3

 To prevent additional environments from being affected, we have disabled the
ability to upgrade existing environments to these versions and to create new
environments using these versions. If your environment is already using one of
these versions, you can continue to use it as usual. We are working to resolve
the issue for all currently affected environments.

説明:
最近リリースされたCloud Composerの以下のバージョンにおいて、メトリックレポートに影響を与える可能性のある問題が発見されました。

*   `composer-2.15.4-airflow-*`
*   `composer-3-airflow-2.10.5-build.20`
*   `composer-3-airflow-2.9.3-build.40`
*   `composer-3-airflow-3.1.0-build.3`

この問題がさらに多くの環境に影響することを防ぐため、現在、これらの問題のあるバージョンへの既存環境のアップグレード、および新規環境の作成が一時的に無効化されています。もしお使いの環境が既にこれらのバージョンのいずれかを使用している場合でも、引き続き通常通り利用できます。Google Cloudは、現在影響を受けているすべての環境について問題を解決するために取り組んでいます。

影響有無:
影響はありません。

理由:
お客様が現在ご利用中のCloud Composerのバージョンは `2.7.1` であり、Apache Airflowのバージョンは `2.7.3` です。
リリースノートに記載されている問題のあるCloud Composerのバージョンリスト（`2.15.4`、`3-airflow-2.10.5`、`3-airflow-2.9.3`、`3-airflow-3.1.0`）には、お客様の環境バージョン `2.7.1` は含まれていません。そのため、現在の稼働環境には直接的な影響はありません。

対処方法:
現在の環境に対する特別な対処は不要です。
将来的にCloud Composerのアップグレードを計画される際には、この問題が解決されたことを確認し、Google Cloudの公式リリースノートやCloud Composerのドキュメントで最新情報をご確認ください。

用語説明:
*   **Cloud Composer**: Google Cloudが提供する、フルマネージドなApache Airflowサービスです。ユーザーはデータパイプラインをオーケストレーションするためのApache Airflow環境を容易に構築・運用できます。
*   **Apache Airflow**: プログラムによってワークフロー（DAGs: Directed Acyclic Graphs）をオーサリング、スケジューリング、監視するためのオープンソースプラットフォームです。
*   **メトリックレポート (Metrics Reporting)**: システムやアプリケーションのパフォーマンス、健全性、リソース使用状況などを示す数値データ（メトリック）を収集し、モニタリングシステム（例: Google Cloud Monitoring）に送信する機能です。これにより、システムの稼働状況を可視化し、異常を検知することが可能になります。
*   **`composer-X.Y.Z-airflow-A.B.C`**: Cloud Composerの環境バージョンを示します。`X.Y.Z` はCloud Composerのバージョンを、`A.B.C` はそのComposer環境にバンドルされているApache Airflowのバージョンを示します。
# Title: November 21, 2025 
Link: https://docs.cloud.google.com/release-notes#November_21_2025<br>
ご担当者様

Google Cloudのリリースノートに関するお問い合わせ、ありがとうございます。
以下に、各製品ごとの影響評価と対処方法をまとめました。

---

# Apigee X
## Issue
原文:
Message Processor returns 500 error with `"Duplicate Header "authorization""`.
When multiple authorization headers are present in a request, the Apigee ingress gateway
doesn't concatenate them into a single header. This results in the Message Processor
returning a `500` error with a `"Duplicate Header "authorization""` message.
For more information, see Apigee known issues.
[Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues)

説明：
クライアントからのリクエストに複数の `Authorization` ヘッダーが含まれる場合、Apigeeのingress gatewayがこれらのヘッダーを単一のヘッダーに結合せずにMessage Processorに渡すため、Message Processorが`"Duplicate Header "authorization""`というメッセージと共にHTTP 500エラーを返すという既知の問題です。

影響有無：
**影響あり**
Apigee X環境をご利用中で、クライアントアプリケーションがHTTPリクエストに複数の `Authorization` ヘッダーを誤って、または意図的に含めて送信する可能性がある場合に影響します。APIの仕様やクライアントの実装によっては、この問題によりAPIコールが失敗する可能性があります。

対処方法：
この問題に対する直接的な修正パッチのリリース情報はありませんが、以下のいずれかの方法を検討してください。
1.  **クライアント側の修正:** 最も推奨される方法として、APIを呼び出すクライアントアプリケーションが単一の`Authorization`ヘッダーのみを送信するように修正を依頼します。これはHTTPプロトコルのベストプラクティスに沿っています。
2.  **Apigeeポリシーによるヘッダー処理:** Apigee APIプロキシのPreFlowまたはTargetEndpoint PreFlowにおいて、JavaScriptポリシーやAssignMessageポリシーを使用して、複数の`Authorization`ヘッダーを処理（例: 最初の一つだけを使用する、結合する、またはエラーを返す）するロジックを実装することを検討します。
3.  **Apigee Known Issuesの確認:** リリースノートに記載されているApigee Known Issuesのドキュメント（[Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues)）で、より具体的な回避策や修正に関する情報が提供されていないか定期的に確認してください。

用語説明：
*   **Apigee X:** Google Cloudが提供するフルマネージドのAPI管理プラットフォームです。APIの設計、セキュリティ、分析、スケーリングをサポートします。
*   **Message Processor:** Apigeeのランタイムコンポーネントの一部で、受信したAPIリクエストを処理し、ポリシーを実行し、バックエンドサービスにルーティングする役割を担います。
*   **Ingress Gateway:** Apigeeエッジ環境において、外部からのAPIリクエストを受け取るエントリポイントとなるゲートウェイコンポーネントです。
*   **HTTP Authorization Header:** HTTP/1.1プロトコルにおいて、クライアントが認証情報（例: Bearerトークン、Basic認証）をサーバーに送信するために使用する標準ヘッダーです。

---

# Google Kubernetes Engine
## Issue
原文:
GKE versions earlier than 1.32 don't support
direct NFS volume mounts
to NFS volumes that exclusively use an NFS protocol greater than `NFSv4.0`.
[direct NFS volume mounts](https://kubernetes.io/docs/concepts/storage/volumes/#nfs)
When using direct NFS volume mounts, Pods on GKE node versions
earlier than 1.32 might fail to mount NFS volumes that are configured to only
support protocols greater than `NFSv4.0` (such as `NFSv4.1` or `NFSv4.2`). This
issue occurs because the `containerized_mounter` on these earlier
GKE versions uses version `1.2.8` of the `nfs-utils` package,
which doesn't support `NFSv4` minor versions. As a result, the mount process
fails with the `mount.nfs: access denied by server` error message.
This issue doesn't affect GKE version 1.32 and later, which
include an updated version of the `nfs-utils` package. To resolve this issue,
try one of the following options:
*   Upgrade clusters to GKE version 1.32 or later.
*   Configure the NFS volume to support both the `NFSv3` and `NFSv4` protocols,
    which allows the mount to succeed by falling back to a compatible version.
*   Use a PersistentVolume and PersistentVolumeClaim to mount the NFS volume,
    which allows for explicit NFS version specification.

説明：
GKEバージョン1.32より前のノードを使用している場合、`NFSv4.0`より新しいプロトコル（例: `NFSv4.1`、`NFSv4.2`）のみをサポートするように設定されたNFSボリュームへの直接マウントができないという問題です。これは、古いGKEバージョンで使用されている`nfs-utils`パッケージが`NFSv4`のマイナーバージョンをサポートしていないため、マウントが`mount.nfs: access denied by server`エラーで失敗します。GKEバージョン1.32以降では、この問題は`nfs-utils`パッケージの更新により解消されています。

影響有無：
**影響あり**
現在GKEバージョン1.32未満のクラスターをご利用中で、かつPodが直接NFSボリュームをマウントしており、そのNFSボリュームが`NFSv4.1`や`NFSv4.2`などの`NFSv4.0`より新しいプロトコルのみをサポートしている場合に影響します。`PersistentVolume`と`PersistentVolumeClaim`を使用している場合は、NFSバージョンを明示的に指定できるため、この問題の影響を受けにくい可能性があります。

対処方法：
以下のいずれかの方法で対応してください。
1.  **GKEクラスターのアップグレード:** 最も推奨される解決策は、GKEクラスターをバージョン1.32以降にアップグレードすることです。これにより、`nfs-utils`パッケージが更新され、この問題が解消されます。
2.  **NFSボリュームのプロトコル設定変更:** NFSサーバー側で、`NFSv3`と`NFSv4`の両方のプロトコルをサポートするように設定を変更します。これにより、クライアントが互換性のあるバージョンにフォールバックしてマウントできるようになります。
3.  **PersistentVolumeとPersistentVolumeClaimの使用:** 直接NFSマウントではなく、Kubernetesの`PersistentVolume`と`PersistentVolumeClaim`を使用してNFSボリュームをマウントするようにワークロードを変更します。これにより、NFSバージョンを明示的に指定できるようになります。

用語説明：
*   **GKE (Google Kubernetes Engine):** Google Cloud上で動作するマネージドなKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **NFS (Network File System):** ネットワークを通じてファイルシステムを共有するための分散ファイルシステムプロトコルです。
*   **Direct NFS volume mounts:** Kubernetes Pod定義内で直接NFS共有をボリュームとして指定し、マウントする方式です。
*   **PersistentVolume (PV) / PersistentVolumeClaim (PVC):** Kubernetesにおける永続ストレージを抽象化するためのAPIオブジェクトです。PVはクラスター内のストレージリソースを表し、PVCはユーザーがそのストレージを要求する手段です。これらを使用することで、Podは具体的なストレージの実装に依存せずに永続データを扱えます。
*   **`nfs-utils`:** NFSクライアントおよびサーバーのユーティリティプログラム群を含むパッケージです。NFSボリュームのマウントや管理に必要です。

## Issue
原文:
In GKE versions 1.34.1-gke.2037001 and 1.34.1-gke.2541000, Arm
nodes that use an Ubuntu node image might incorrectly use an image with a
64 KB page size instead of the default 4 KB page size. Avoid using
version 1.34.1-gke.2037001 and 1.34.1-gke.2541000 for your Ubuntu Arm nodes.

説明：
GKEバージョン1.34.1-gke.2037001および1.34.1-gke.2541000において、Ubuntuノードイメージを使用するArmノードが、デフォルトの4KBページサイズではなく、誤って64KBページサイズのイメージでプロビジョニングされる可能性があるという問題です。

影響有無：
**影響あり**
対象のGKEバージョン（1.34.1-gke.2037001または1.34.1-gke.2541000）で、ArmノードプールにUbuntuノードイメージを使用している場合に影響します。ページサイズが異なることで、特定のアプリケーションのパフォーマンス特性に影響を与えたり、互換性の問題を引き起こしたりする可能性があります（特にメモリ割り当てやI/Oパターンに敏感なワークロード）。

対処方法：
この問題が発生するGKEバージョンを避けることが推奨されています。
1.  **対象バージョンの回避:** ArmノードプールでUbuntuノードイメージを使用する際は、GKEバージョン1.34.1-gke.2037001および1.34.1-gke.2541000の使用を避けてください。
2.  **バージョンアップグレードまたはダウングレード:** 既にこれらのバージョンを使用している場合は、この問題が修正されたより新しい安定版バージョン、または問題のなかった以前のバージョンへのアップグレードまたはダウングレードを検討してください。
3.  **ノードイメージの変更:** Ubuntu以外のノードイメージ（例: Container-Optimized OS (COS)）の使用を検討してください。COSイメージではこの問題が発生しない可能性があります。

用語説明：
*   **Arm nodes:** ArmアーキテクチャのCPUを搭載したGKEワーカーノードです。特定のワークロードにおいて、x86ベースのノードよりも優れたコストパフォーマンスを提供する場合があります。
*   **Ubuntu node image:** GKEノードの基盤オペレーティングシステムとしてUbuntu Linuxディストリビューションを使用するノードイメージです。
*   **Page size (ページサイズ):** オペレーティングシステムが仮想メモリを管理するための最小単位です。通常、一般的なシステムでは4KBがデフォルトですが、一部のCPUアーキテクチャや特定の用途では64KBなどのより大きなページサイズが使用されることがあります。ページサイズの違いは、メモリ管理効率、キャッシュ利用率、アプリケーションのパフォーマンスに影響を与える可能性があります。

---
ご不明な点がございましたら、お気軽にお問い合わせください。