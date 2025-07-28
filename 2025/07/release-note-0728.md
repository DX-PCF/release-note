
# Title: July 25, 2025 
Link: https://cloud.google.com/release-notes#July_25_2025<br>
Google Cloud のリリースノートに基づき、構築済みのサービスへの影響有無を調査しました。

---

# Compute Engine
## Changed
原文: Hyperdisk Extreme is available in all regions and zones.
For more information, see About Hyperdisk Extreme.

説明: Hyperdisk Extremeが全てのリージョンとゾーンで利用可能になりました。これにより、より多くの地理的ロケーションで高性能なブロックストレージオプションを選択できるようになります。
影響有無: なし
理由: これは新機能の利用可能範囲の拡大であり、既存のHyperdisk Extremeの利用や他のディスクタイプに影響を与えるものではありません。
対処方法: なし。必要に応じて、将来的にHyperdisk Extremeの利用を検討する際に、選択肢が広がったことを考慮してください。

## Changed
原文: You can now resize Hyperdisk Balanced volumes twice within a 4-hour window. For more information, see Capacity changes.

説明: Hyperdisk Balanced ボリュームのリサイズ（容量変更）操作が、4時間以内に2回まで可能になりました。これまでは、リサイズ操作後、一定期間再度のリサイズが制限されていましたが、この制限が緩和され、より柔軟な容量調整が可能になります。
影響有無: なし
理由: これは既存機能の改善であり、リサイズ操作の利便性が向上します。現在のストレージ構成や運用に直接的な影響はありません。
対処方法: なし。将来的にHyperdisk Balancedの容量調整が必要になった際に、この新しい柔軟性を活用できます。

# Google Kubernetes Engine
## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

 - Version 1.33.2-gke.1111000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
  - 1.28.15-gke.2488000
  - 1.29.15-gke.1656000
  - 1.30.12-gke.1340000
  - 1.31.10-gke.1034000
  - 1.32.6-gke.1025000
  - 1.33.2-gke.1240000
- The following versions are no longer available in the Extended channel:
  - (多数のバージョンリスト)
- Auto-upgrade targets are now available for the following minor versions:
  - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2456000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
  - (各マイナーバージョンごとのパッチバージョンアップグレードターゲットリスト)

説明: GKEのExtendedリリースチャネルにおいて、新しいバージョンの提供開始、古いバージョンの提供終了、クラスタ作成時のデフォルトバージョンの変更、および自動アップグレードのターゲットバージョンが更新されました。特に、バージョン1.33.2-gke.1111000がExtendedチャネルでのクラスタ作成時のデフォルトバージョンになり、自動アップグレードでは1.27から1.28へのアップグレードが開始されます。
影響有無: なし
理由: 
- 当社のGoogle Cloud Composer2 (Compoer version 2.7.1) は、Googleが管理するGKEクラスタ上で動作します。Composerが利用しているGKEバージョンは、Google Cloud Composer側で互換性が考慮されており、本リリースノートに直接的な破壊的変更は含まれていません。
- Composer環境の基盤となるGKEクラスタがExtendedチャネルを使用しており、自動アップグレードが有効な場合、メンテナンスウィンドウ中にGKEのバージョンが更新される可能性があります。Composer 2.7.1は通常GKE 1.27.xまたは1.28.xを利用しているため、GKE 1.27.xを利用している場合はGKE 1.28.xへの自動アップグレード対象となります。
対処方法: 
- 現在ご利用中のComposer環境が属するGKEのリリースチャネル、現在のGKEバージョン、自動アップグレード設定、およびメンテナンスウィンドウ設定を確認してください。
- GKEのバージョンアップはGoogle Cloud Composerの管理下で行われますが、念のためアップグレード後にワークロードの動作に異常がないか監視を強化することをお勧めします。

## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

 - Version 1.33.2-gke.1111000 is now the default version for cluster creation.
- The following versions are now available:
  - 1.30.12-gke.1390000
  - 1.31.11-gke.1002000
  - 1.32.6-gke.1096000
  - 1.33.2-gke.4655000
- The following node versions are now available:
  - (多数のバージョンリスト)
- The following versions are no longer available:
  - (多数のバージョンリスト)
- Auto-upgrade targets are now available for the following minor versions:
  - (各マイナーバージョンごとのアップグレードターゲットリスト)
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
  - (各マイナーバージョンごとのパッチバージョンアップグレードターゲットリスト)

説明: GKEのデフォルトチャネルにおいて、新しいバージョンの提供開始、古いバージョンの提供終了、クラスタ作成時のデフォルトバージョンの変更、および自動アップグレードのターゲットバージョンが更新されました。バージョン1.33.2-gke.1111000がクラスタ作成時のデフォルトバージョンになります。
影響有無: なし
理由: 
- 当社のGoogle Cloud Composer2 (Compoer version 2.7.1) は、Googleが管理するGKEクラスタ上で動作します。Composerが利用しているGKEバージョンは、Google Cloud Composer側で互換性が考慮されており、本リリースノートに直接的な破壊的変更は含まれていません。
- Composer環境の基盤となるGKEクラスタがデフォルトチャネルを使用しており、自動アップグレードが有効な場合、メンテナンスウィンドウ中にGKEのバージョンが更新される可能性があります。
対処方法: 
- 現在ご利用中のComposer環境が属するGKEのリリースチャネル、現在のGKEバージョン、自動アップグレード設定、およびメンテナンスウィンドウ設定を確認してください。
- GKEのバージョンアップはGoogle Cloud Composerの管理下で行われますが、念のためアップグレード後にワークロードの動作に異常がないか監視を強化することをお勧めします。

## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

 - Version 1.33.2-gke.1240000 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
  - 1.30.12-gke.1390000
  - 1.31.11-gke.1002000
  - 1.32.6-gke.1096000
  - 1.33.2-gke.4655000
- The following versions are no longer available in the Rapid channel:
  - (多数のバージョンリスト)
- Auto-upgrade targets are now available for the following minor versions:
  - (各マイナーバージョンごとのアップグレードターゲットリスト)
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
  - (各マイナーバージョンごとのパッチバージョンアップグレードターゲットリスト)

説明: GKEのRapidリリースチャネルにおいて、新しいバージョンの提供開始、古いバージョンの提供終了、クラスタ作成時のデフォルトバージョンの変更、および自動アップグレードのターゲットバージョンが更新されました。バージョン1.33.2-gke.1240000がRapidチャネルでのクラスタ作成時のデフォルトバージョンになります。
影響有無: なし
理由: 
- 当社のGoogle Cloud Composer2 (Compoer version 2.7.1) は、Googleが管理するGKEクラスタ上で動作します。Composerが利用しているGKEバージョンは、Google Cloud Composer側で互換性が考慮されており、本リリースノートに直接的な破壊的変更は含まれていません。
- Composer環境の基盤となるGKEクラスタがRapidチャネルを使用しており、自動アップグレードが有効な場合、メンテナンスウィンドウ中にGKEのバージョンが更新される可能性があります。
対処方法: 
- 現在ご利用中のComposer環境が属するGKEのリリースチャネル、現在のGKEバージョン、自動アップグレード設定、およびメンテナンスウィンドウ設定を確認してください。
- GKEのバージョンアップはGoogle Cloud Composerの管理下で行われますが、念のためアップグレード後にワークロードの動作に異常がないか監視を強化することをお勧めします。

## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

 - Version 1.33.2-gke.1111000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
  - 1.30.12-gke.1340000
  - 1.31.10-gke.1034000
  - 1.32.6-gke.1025000
  - 1.33.2-gke.1240000
- The following versions are no longer available in the Regular channel:
  - (多数のバージョンリスト)
- Auto-upgrade targets are now available for the following minor versions:
  - (各マイナーバージョンごとのアップグレードターゲットリスト)
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
  - (各マイナーバージョンごとのパッチバージョンアップグレードターゲットリスト)

説明: GKEのRegularリリースチャネルにおいて、新しいバージョンの提供開始、古いバージョンの提供終了、クラスタ作成時のデフォルトバージョンの変更、および自動アップグレードのターゲットバージョンが更新されました。バージョン1.33.2-gke.1111000がRegularチャネルでのクラスタ作成時のデフォルトバージョンになります。
影響有無: なし
理由: 
- 当社のGoogle Cloud Composer2 (Compoer version 2.7.1) は、Googleが管理するGKEクラスタ上で動作します。Composerが利用しているGKEバージョンは、Google Cloud Composer側で互換性が考慮されており、本リリースノートに直接的な破壊的変更は含まれていません。
- Composer環境の基盤となるGKEクラスタがRegularチャネルを使用しており、自動アップグレードが有効な場合、メンテナンスウィンドウ中にGKEのバージョンが更新される可能性があります。
対処方法: 
- 現在ご利用中のComposer環境が属するGKEのリリースチャネル、現在のGKEバージョン、自動アップグレード設定、およびメンテナンスウィンドウ設定を確認してください。
- GKEのバージョンアップはGoogle Cloud Composerの管理下で行われますが、念のためアップグレード後にワークロードの動作に異常がないか監視を強化することをお勧めします。

## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

 - Version 1.32.4-gke.1698000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:
  - 1.30.12-gke.1320000
  - 1.31.9-gke.1287000
  - 1.32.4-gke.1767000
  - 1.33.2-gke.1043000
- The following versions are no longer available in the Stable channel:
  - (多数のバージョンリスト)
- Auto-upgrade targets are now available for the following minor versions:
  - (各マイナーバージョンごとのアップグレードターゲットリスト)
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
  - (各マイナーバージョンごとのパッチバージョンアップグレードターゲットリスト)

説明: GKEのStableリリースチャネルにおいて、新しいバージョンの提供開始、古いバージョンの提供終了、クラスタ作成時のデフォルトバージョンの変更、および自動アップグレードのターゲットバージョンが更新されました。バージョン1.32.4-gke.1698000がStableチャネルでのクラスタ作成時のデフォルトバージョンになります。
影響有無: なし
理由: 
- 当社のGoogle Cloud Composer2 (Compoer version 2.7.1) は、Googleが管理するGKEクラスタ上で動作します。Composerが利用しているGKEバージョンは、Google Cloud Composer側で互換性が考慮されており、本リリースノートに直接的な破壊的変更は含まれていません。
- Composer環境の基盤となるGKEクラスタがStableチャネルを使用しており、自動アップグレードが有効な場合、メンテナンスウィンドウ中にGKEのバージョンが更新される可能性があります。
対処方法: 
- 現在ご利用中のComposer環境が属するGKEのリリースチャネル、現在のGKEバージョン、自動アップグレード設定、およびメンテナンスウィンドウ設定を確認してください。
- GKEのバージョンアップはGoogle Cloud Composerの管理下で行われますが、念のためアップグレード後にワークロードの動作に異常がないか監視を強化することをお勧めします。

## Changed
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following Kubernetes versions are now available for new clusters and for opt-in control plane upgrades and node upgrades for existing clusters. For more information on versioning and upgrades, see GKE versioning and support and Upgrades.

説明: GKEクラスタのバージョンが更新され、新しいバージョンがクラスタの新規作成および既存クラスタのアップグレードで利用可能になりました。これは、GKEのバージョン管理とアップグレードに関する一般的なアナウンスです。
影響有無: なし
理由: 
- 当社のGoogle Cloud Composer2 (Compoer version 2.7.1) は、Googleが管理するGKEクラスタ上で動作します。Composerが利用しているGKEバージョンは、Google Cloud Composer側で互換性が考慮されており、本リリースノートに直接的な破壊的変更は含まれていません。
- GKEのバージョン更新は、Google Cloud Composerサービスが自動的に管理するGKEクラスタに適用される可能性がありますが、Composerサービスの安定性には影響を与えないように設計されています。
対処方法: 
- Composer環境のGKEバージョン、リリースチャネル、自動アップグレード設定、およびメンテナンスウィンドウ設定を定期的に確認し、GKEのバージョンライフサイクルとComposerの対応バージョンを把握しておくことを推奨します。

---

### 用語説明

*   **Hyperdisk Extreme**: Google Cloud Compute Engineが提供する高性能なブロックストレージタイプで、非常に高いIOPS（Input/Output Operations Per Second）とスループットを提供します。特に、データベースなどのレイテンシに敏感なワークロードに適しています。
*   **Hyperdisk Balanced**: Hyperdisk Extremeよりは劣るものの、従来のPersistent Disk（SSD）よりも高いパフォーマンスとコスト効率のバランスが取れたブロックストレージタイプです。多様なワークロードに適しています。
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **GKE リリースチャネル (Release Channel)**: GKEクラスタが受け取る更新の頻度と安定性を制御するための仕組みです。「Rapid」「Regular」「Stable」「Extended」などのチャネルがあり、それぞれ新機能の導入ペースやパッチの適用頻度が異なります。
    *   **Rapid**: 最新機能が最も早く提供されますが、安定性リスクが最も高くなります。
    *   **Regular**: 新機能と安定性のバランスが取れたチャネルです。
    *   **Stable**: 安定性が最優先され、十分にテストされたバージョンが提供されます。
    *   **Extended**: 特定のGKEバージョンに対して長期間のサポートを提供し、延長されたサポート期間（最長3年）が適用されます。
*   **自動アップグレード (Auto-upgrade)**: GKEクラスタのコントロールプレーンやノードが、指定されたメンテナンスウィンドウ内に自動的に最新のパッチバージョンやマイナーバージョンにアップグレードされる機能です。
*   **メンテナンスウィンドウ (Maintenance Window)**: GKEクラスタの自動メンテナンス（アップグレードなど）が実行される時間帯を指定する機能です。これにより、ワークロードへの影響を最小限に抑えることができます。
*   **Google Cloud Composer**: Google Cloud上でApache Airflowを実行するためのフルマネージドサービスです。ワークフローの作成、スケジューリング、監視を容易にします。Composer環境は内部的にGKEクラスタを利用しています。