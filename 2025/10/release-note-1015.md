
# Title: October 14, 2025 
Link: https://cloud.google.com/release-notes#October_14_2025<br>
はい、承知いたしました。Google Cloudのリリースノートに基づいて、各製品への影響調査結果を専門的な言葉遣いと書式設定で回答します。

---

# BigQuery

## Announcement

**原文:**
The BigQuery Data Transfer API (bigquerydatatransfer.googleapis.com) is now enabled by default for every new Google Cloud project. This feature is generally available (GA).

**説明:**
BigQuery Data Transfer API (`bigquerydatatransfer.googleapis.com`) が、新規に作成される全てのGoogle Cloudプロジェクトにおいて、デフォルトで有効化されるようになりました。この機能は一般提供 (GA) されています。

**影響有無:**
*   **新規プロジェクト:** BigQuery Data Transfer APIがデフォルトで有効化されるため、手動でAPIを有効化する手間が省けます。これにより、データ転送設定のセットアップがより迅速に行えるようになり、利便性が向上します。セキュリティの観点では、不要なAPIが有効化されるリスクはありますが、BigQuery Data Transferは幅広いデータ統合シナリオで利用されるため、通常は許容範囲内の変更と考えられます。
*   **既存プロジェクト:** 既存のGoogle Cloudプロジェクトに対しては、この変更による影響はありません。APIの有効化状態は現在の設定から変更されません。

**対処方法:**
通常、対処は不要です。
もし、新規プロジェクトでBigQuery Data Transfer APIの有効化を厳密に制御したい、あるいはデフォルトで有効化されることを避けたい場合は、プロジェクト作成後にIAMや組織ポリシーを用いてAPIの無効化やアクセス制御を検討することは可能です。しかし、一般的なユースケースでは、このデフォルト有効化は利便性の向上に寄与します。

**用語説明:**
*   **BigQuery Data Transfer API**: Google Cloud BigQueryに、様々なサードパーティ製アプリケーション（Google Ads、YouTube、Amazon S3など）やGoogleのサービスから、スケジュールに基づいてデータを自動的に転送するための機能を提供するAPIです。ETL（Extract, Transform, Load）プロセスにおけるデータロード部分の自動化に利用されます。
*   **一般提供 (GA: Generally Available)**: Google Cloudのプロダクトや機能が、安定した状態にあり、SLA（Service Level Agreement）が適用され、本番環境での利用が推奨される段階を指します。

---

# Google Kubernetes Engine

## Issue

**原文:**
In GKE versions 1.32.4-gke.1029000 and later, MountVolume calls for network file system (NFS) volumes might fail with the following error: `mount.nfs:rpc.statd is not running but is required for remote locking`.

This failure can occur if a Pod mounting an NFS volume runs on the same node as an NFS server Pod, and the NFS server Pod starts before the client Pod attempts to mount the volume. This scenario causes a conflict over the `rpcbind` service, which prevents the service from starting correctly on the node for the client Pod, leading to the mount failure.

As a workaround, deploy this DaemonSet on all nodes where you mount the NFS volumes. The DaemonSet ensures that the required services start correctly.

**説明:**
GKEバージョン1.32.4-gke.1029000以降において、NFS (Network File System) ボリュームのマウント操作 (`MountVolume` calls) が「`mount.nfs:rpc.statd is not running but is required for remote locking`」というエラーメッセージとともに失敗する可能性があるという既知の不具合です。

この問題は、NFSボリュームをマウントするクライアントPodとNFSサーバーPodが同じノード上で動作し、かつNFSサーバーPodがクライアントPodより先に起動した場合に発生します。この状況下では、`rpcbind` サービスに関して競合が発生し、クライアントPod側のノードで必要なサービスが正しく起動できず、結果としてNFSマウントが失敗します。

この問題に対するワークアラウンドとして、NFSボリュームをマウントする全てのノードに、特定のDaemonSetをデプロイすることが推奨されています。このDaemonSetは、必要なサービスが正しく起動することを保証します。

**影響有無:**
*   **影響あり:**
    *   GKEバージョンが1.32.4-gke.1029000以降である環境。
    *   NFSボリュームを使用しているアプリケーションが存在する環境。
    *   特に、NFSサーバーPodとNFSクライアントPodが同一ノードにスケジュールされる可能性がある構成の場合、NFSマウントの失敗により、アプリケーションのストレージアクセスが妨げられ、サービスが停止または機能不全に陥る可能性があります。
*   **影響なし:**
    *   上記バージョンより古いGKEを使用している場合。
    *   NFSボリュームを一切使用していない環境。
    *   NFSサーバーとNFSクライアントが厳密に異なるノードプールやノードに分離されており、同一ノードへのスケジュールが絶対に発生しないことが保証される環境。

**対処方法:**
対象のGKEバージョンを利用しており、NFSボリュームを運用している場合は、以下のワークアラウンドを適用してください。

1.  **DaemonSetのデプロイ:** リリースノートで示されている[DaemonSet](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/troubleshooting/nfs-mount-workaround/daemonset.yaml)を、NFSボリュームをマウントする全てのGKEノードにデプロイします。
    *   DaemonSetのYAMLファイルの内容を確認し、必要であれば環境に合わせて調整します。
    *   `kubectl apply -f daemonset.yaml` コマンドを使用して、GKEクラスタにDaemonSetをデプロイします。
2.  **監視:** DaemonSetが正しくデプロイされ、各ノードでNFS関連のサービスが適切に動作しているかを確認します。
3.  **今後のGKEアップデートの確認:** この問題は既知の不具合であるため、今後のGKEバージョンアップで修正される可能性があります。定期的にGKEのリリースノートを確認し、修正がリリースされた場合は、このワークアラウンドのDaemonSetの停止または削除を検討してください。

**用語説明:**
*   **NFS (Network File System)**: ネットワーク越しにファイルシステムを共有するための分散ファイルシステムプロトコルです。Kubernetes環境では、Podが永続的な共有ストレージとしてNFSサーバーに接続し、ボリュームをマウントして利用することがあります。
*   **`rpc.statd` / `rpcbind`**: NFSが正しく機能するために必要なRPC (Remote Procedure Call) サービスの一部です。
    *   `rpcbind` は、RPCプログラム番号をネットワークアドレスにマッピングするサービスであり、クライアントがRPCベースのサービスに接続するための最初のステップとなります。
    *   `rpc.statd` は、NFSv3までのロック管理（Network Lock Manager, NLM）に関連するデーモンです。これらのサービスが正常に動作しないと、NFSクライアントはボリュームを適切にマウントできません。
*   **DaemonSet**: Kubernetesのコントローラの一種で、クラスター内の全ノード（または指定されたノードのサブセット）でPodのコピーが1つだけ実行されることを保証します。各ノードでログ収集エージェントや監視エージェント、ストレージプロキシなどのシステムレベルのユーティリティを実行する際に用いられます。
*   **MountVolume**: KubernetesのPodが、PersistentVolumeClaim (PVC) などによって定義されたボリュームを、Pod自身のファイルシステム内にマウントする操作を指します。