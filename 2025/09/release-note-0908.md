
# Title: September 04, 2025 
Link: https://cloud.google.com/release-notes#September_04_2025<br>
## Apigee X

### Announcement

原文: On September 4, 2025, we released an updated version of Apigee.
説明: 2025年9月4日にApigeeの更新版がリリースされたというアナウンスです。具体的な変更内容（新機能、変更点、非互換性など）は、このアナウンスでは言及されていません。
影響有無: 現時点での直接的な影響は不明です。このアナウンス自体は将来のリリースを示唆しており、現行のサービスへの即時的な影響はありません。
対処方法: 今後の詳細なリリースノートや変更点のアナウンスを注視し、サービスへの影響を評価してください。

---

## Cloud SQL for PostgreSQL

### Changed

原文: The release note on August 13, 2025 regarding Private Service Connect (PSC) outbound connectivity has been updated. PSC outbound connectivity is required for homogeneous migrations to PSC-enabled Cloud SQL instances using Database Migration Service. For more information, see PSC outbound connections.
説明: 2025年8月13日付のPrivate Service Connect (PSC) アウトバウンド接続に関するリリースノートが更新されました。この更新により、Database Migration Service (DMS) を使用して、PSCが有効なCloud SQLインスタンスへの同種移行（homogeneous migrations）を行う場合、PSCアウトバウンド接続の確立が必須となることが明確化されました。
影響有無:
*   現在、Cloud SQL for PostgreSQLを利用しており、かつ将来的にDatabase Migration Service (DMS) を利用してPSC有効なCloud SQLインスタンスへの「同種移行」を計画している場合に影響があります。
*   DMSを利用した同種移行を計画していない場合や、すでに移行が完了している場合は、直接的な影響はありません。
対処方法:
*   DMSを利用してPSC有効なCloud SQLインスタンスへの同種移行を計画している場合は、移行元の環境からPSCアウトバウンド接続が確立できるようにネットワーク構成を検討し、必要な準備を進める必要があります。詳細は、リンクされている「PSC outbound connections」ドキュメントを参照してください。
用語説明:
*   **Private Service Connect (PSC)**: Google Cloudのプライベートネットワーク内で、サービスコンシューマー（あなたのVPCネットワーク）からサービスプロデューサー（Cloud SQLなどのGoogleマネージドサービス）へ、プライベートIPアドレスを介してセキュアに接続するための技術です。インターネットを経由せず、VPC内部で接続が完結します。
*   **アウトバウンド接続 (Outbound Connectivity)**: サービスコンシューマーのVPCネットワークから、サービスプロデューサーのVPCネットワークへ向けて開始される接続のことです。
*   **Database Migration Service (DMS)**: データベースの移行プロセスを自動化・簡素化するGoogle Cloudのサービスです。オンプレミスや他のクラウドのデータベースからCloud SQLなどのGoogle Cloudデータベースへの移行をサポートします。
*   **同種移行 (Homogeneous Migrations)**: 移行元と移行先のデータベースシステムが同じ種類である移行を指します（例: PostgreSQLからPostgreSQLへの移行）。

---

## Google Kubernetes Engine

### Changed

原文: **CNI spec version for GKE Dataplane V2 updated to v1.1.0**
Starting with GKE patch version 1.34, clusters using GKE Dataplane V2 are being updated from CNI spec v0.3.1 to v1.1.0. Action required: If you use your own CNI plugins in your GKE cluster (such as self-managed open-source Istio), you must upgrade them to a version compatible with CNI spec v1.1.0 to prevent errors.
説明: GKE Dataplane V2を使用しているGKEクラスタにおいて、GKEパッチバージョン1.34以降、CNI (Container Network Interface) の仕様がv0.3.1からv1.1.0に更新されます。もしGKEクラスタ内で独自のCNIプラグイン（例えば、自己管理型のオープンソースIstioなど）を使用している場合、エラーを防ぐためにCNI仕様v1.1.0と互換性のあるバージョンにアップグレードする必要があります。
影響有無:
*   **影響あり**: GKE Dataplane V2を有効にしているGKEクラスタで、かつ、カスタムCNIプラグイン（例: 自己管理型のオープンソースIstio）をデプロイしている場合に影響があります。
*   **影響なし**: GKE Dataplane V2を使用していない、またはGKEに標準で組み込まれているネットワーク機能のみを利用しており、カスタムCNIプラグインを使用していない場合は影響ありません。
    *   Composer (Composer version 2.7.1, Airflow version 2.7.3) を利用している環境では、基盤のGKEはGoogleが管理するため、通常ユーザーがカスタムCNIプラグインを直接デプロイすることはありません。したがって、ユーザー側での直接的な対処は不要ですが、Composerの内部動作に影響がないかはGoogle側で対応されると想定されます。
対処方法:
*   影響がある場合、クラスタがGKEバージョン1.34に更新される前に、使用しているカスタムCNIプラグインがCNI仕様v1.1.0と互換性があることを確認し、必要に応じてアップグレードしてください。
用語説明:
*   **GKE Dataplane V2**: Google Kubernetes Engineにおけるネットワークデータプレーンの新しい実装で、eBPF (extended Berkeley Packet Filter) とCiliumをベースにしています。これにより、ネットワークのパフォーマンス、可視性、セキュリティが向上します。
*   **CNI (Container Network Interface)**: Linuxコンテナのネットワーク構成を標準化するための仕様です。KubernetesのPodがどのようにネットワークと通信するかを定義し、多様なネットワークプラグインをサポートします。
*   **CNIプラグイン**: CNI仕様に準拠したネットワーク実装を提供するソフトウェアです。

### Announcement

原文: **Kubernetes 1.34 is now available in the Rapid channel**
Kubernetes 1.34 is now available in the Rapid channel. For more information about the content of Kubernetes 1.34, read the Kubernetes 1.34 Release Notes.
説明: Kubernetes 1.34がGKEのRapidチャネルで利用可能になりました。Kubernetes 1.34の変更内容に関する詳細は、Kubernetesの公式リリースノートを参照してください。
影響有無:
*   現時点ではRapidチャネルでの提供開始のアナウンスであり、既存のGKEクラスタにはすぐに影響はありません。
*   将来的にKubernetesバージョン1.34へのアップグレードを計画している場合、そのリリースノートの内容を確認し、ワークロードの互換性や変更点について評価する必要があります。
*   Composer (Composer version 2.7.1, Airflow version 2.7.3) はマネージドサービスであり、基盤のKubernetesバージョンはGoogleが管理します。RapidチャネルのバージョンがComposerに適用されることは稀であるため、現時点での直接的な影響は小さいです。
対処方法:
*   現時点での具体的な対処は不要です。将来的に1.34へのアップグレードを検討する際に、リンクされているKubernetes 1.34のリリースノートを確認し、アプリケーションや構成への影響を評価してください。
用語説明:
*   **Rapid channel**: GKEクラスタのアップグレードチャネルの一つで、最も早く新しいKubernetesバージョンが提供されます。最新機能へのアクセスが早い一方で、安定性についてはより慎重な検証が必要です。本番環境では通常、Stableなどのより安定したチャネルが推奨されます。

### Changed

原文: **Other changes in 1.34**
- **containerd 2.1:** GKE nodes are now upgraded to containerd 2.1. This release includes performance improvements such as faster image downloads. For a complete list of changes, see the official containerd 2.1 release notes.
- **VPA InPlaceOrRecreate**: This version introduces a new InPlaceOrRecreate mode in Vertical Pod Autoscaler (VPA) (Public Preview) powered by In-Place Pod Resize (IPPR/IPPU) that allows automatically rightsizing workloads often without recreating the Pod. This mode ensures seamless service continuity while minimizing costs during idle periods. If you haven't used VPA with your workloads before, enable Vertical Pod Autoscaler on your cluster and then create a VPA Object for a workload.
説明: Kubernetes 1.34のGKEノードにおけるその他の変更点です。
*   **containerd 2.1**: GKEノードのコンテナランタイムがcontainerd 2.1にアップグレードされます。これにより、イメージダウンロードの高速化など、パフォーマンスの改善が期待されます。
*   **VPA InPlaceOrRecreate**: Vertical Pod Autoscaler (VPA) に新しい`InPlaceOrRecreate`モード（Public Preview）が導入されます。このモードはIn-Place Pod Resize (IPPR/IPPU) 機能によって実現され、Podを再作成することなくワークロードのリソースを自動的に最適化（rightsizing）できるようになります。これにより、サービスの中断を最小限に抑えつつ、アイドル時のコスト削減に貢献します。VPAをまだ使用していない場合は、クラスタでVPAを有効化し、ワークロード用にVPAオブジェクトを作成することでこの機能を利用できます。
影響有無:
*   **containerd 2.1**: GKEノードが自動的にアップグレードされるため、ユーザーによる直接的な操作は不要です。主にパフォーマンス向上が期待でき、既存ワークロードへの破壊的な影響はほとんどないと考えられます。
*   **VPA InPlaceOrRecreate**: 新機能の追加であり、既存のワークロードには直接的な影響はありません。この機能を利用することで、リソース最適化とコスト削減のメリットを享受できます。
*   Composer (Composer version 2.7.1, Airflow version 2.7.3) の基盤にもcontainerdのアップグレードが適用される可能性がありますが、マネージドサービスであるため、Google側で互換性が確保されると想定されます。VPAの新機能は、ユーザーが明示的に利用を設定しない限り影響しません。
対処方法:
*   **containerd 2.1**: 特段の対処は不要です。パフォーマンス向上の恩恵を受けられます。
*   **VPA InPlaceOrRecreate**: 新機能の恩恵を受けたい場合、クラスタでVertical Pod Autoscalerを有効化し、適切なVPAオブジェクトを作成してワークロードに適用することを検討してください。Public Preview機能であるため、本番環境への導入前に十分なテストと検証を行うことが推奨されます。
用語説明:
*   **containerd**: CNCF（Cloud Native Computing Foundation）プロジェクトの一つで、コンテナイメージの管理や実行などを担う、軽量かつ堅牢なコンテナランタイムです。
*   **Vertical Pod Autoscaler (VPA)**: Kubernetesのオートスケーラーの一つで、Podの過去のCPUやメモリの使用量に基づいて、Podのリソースリクエストとリミットを自動的に推奨または設定し、リソースの最適化を図ります。
*   **In-Place Pod Resize (IPPR/IPPU)**: Podを再起動することなく、実行中のPodに割り当てられているリソース（CPUやメモリ）を変更できるKubernetesの機能です。

### Deprecated

原文: **Deprecated in 1.34**
The v1beta1 gRPC API between the Kubelet and DRA drivers is deprecated in this release in favor of the v1 API. This API will continue to function but we recommend that all drivers move to the v1 API to prepare for the eventual removal of the v1beta1 API.
説明: KubeletとDRA (Dynamic Resource Allocation) ドライバ間のv1beta1 gRPC APIが非推奨化され、今後はv1 APIの使用が推奨されます。v1beta1 APIは引き続き機能しますが、将来的にこのAPIが削除される可能性があるため、すべてのDRAドライバはv1 APIに移行することが推奨されます。
影響有無:
*   **影響あり**: KubernetesのDRA (Dynamic Resource Allocation) 機能を使用しており、かつv1beta1 APIを使用しているカスタムのDRAドライバをデプロイしている場合に影響があります。
*   **影響なし**: DRA機能を使用していない、または使用しているDRAドライバが既にv1 APIに対応している場合は影響ありません。
*   Composer (Composer version 2.7.1, Airflow version 2.7.3) では、通常ユーザーがKubeletやDRAドライバを直接操作したりデプロイしたりすることはないため、直接的な影響はありません。
対処方法:
*   影響がある場合、使用しているDRAドライバがv1 APIに対応しているか確認し、対応していない場合はv1 APIへの移行を検討するか、提供元にアップデートを問い合わせてください。将来的な非推奨APIの削除に備え、計画的な移行が望ましいです。
用語説明:
*   **Kubelet**: 各Kubernetesノード上で動作するエージェントで、Podがノード上で実行され、健全な状態を保つことを保証します。
*   **DRA (Dynamic Resource Allocation)**: Kubernetesの新しいリソース管理フレームワークで、GPUやFPGAなどの特殊なハードウェアリソースを動的にPodに割り当て、管理するための仕組みを提供します。
*   **gRPC API**: Googleが開発した高性能なオープンソースのRPC (Remote Procedure Call) フレームワークです。ネットワーク上の異なるサービス間で効率的に通信するために使用されます。