
# Title: December 08, 2025 
Link: https://docs.cloud.google.com/release-notes#December_08_2025<br>
# Google Kubernetes Engine

## Fixed

原文: The October 14, 2025 issue in which MountVolume calls for network file system (NFS) volumes might fail is fixed for GKE versions 1.34.1-gke.2877000 and later.

説明：
2025年10月14日に特定された、ネットワークファイルシステム（NFS）ボリュームに対するMountVolume呼び出しが失敗する可能性のある問題が、Google Kubernetes Engine (GKE) のバージョン `1.34.1-gke.2877000` およびそれ以降で修正されました。

影響有無：
ポジティブな影響。
*   **NFSボリュームをGKEクラスタで使用している場合**: MountVolume呼び出しの失敗により、PodがNFSボリュームを正しくマウントできない問題が発生していた可能性があります。今回の修正により、該当バージョンにアップグレードすることでこの問題が解消され、NFSボリュームを利用するワークロードの安定性が向上します。
*   **NFSボリュームをGKEクラスタで使用していない場合**: 影響はありません。
*   **現在稼働中のGKEクラスタのバージョンが `1.34.1-gke.2877000` 以降である場合**: 既にこの修正が適用されているか、今後適用されるため、新たな影響はありません。

対処方法：
*   **NFSボリュームをGKEクラスタで使用しており、かつMountVolumeの失敗による問題が発生している、または将来的な安定性を確保したい場合**:
    *   お使いのGKEクラスタをバージョン `1.34.1-gke.2877000` 以降にアップグレードすることを検討してください。
    *   アップグレードは、GKEのメンテナンスウィンドウに合わせて計画的に実施し、事前にテスト環境での動作確認を推奨します。GKEクラスタのアップグレードについては、[公式ドキュメント](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster)を参照してください。
*   **NFSボリュームをGKEクラスタで使用していない場合、または既に修正対象バージョン以降を使用している場合**:
    *   特に対処は不要です。

用語説明：
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドなKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **NFS (Network File System)**: ネットワーク上で複数のコンピュータがファイルシステムを共有するための分散ファイルシステムプロトコルです。GKEにおいては、外部のNFSサーバを永続ボリュームとしてPodにマウントする際に利用されます。
*   **MountVolume**: Kubernetesにおいて、Podがストレージボリューム（永続ボリュームなど）をコンテナにマウントする操作を指します。これにより、コンテナは外部のストレージにアクセスし、データを読み書きできるようになります。MountVolumeの呼び出しが失敗するということは、Podが目的のストレージにアクセスできない状態を意味します。
*   **バージョン番号 `1.34.1-gke.2877000`**: GKEのバージョン表記は、Kubernetesのアップストリームバージョン（例: `1.34.1`）に、GKE固有のパッチバージョンとビルド番号（例: `-gke.2877000`）が付加された形式です。この番号は、特定の修正が含まれるGKEの具体的なビルドを示します。