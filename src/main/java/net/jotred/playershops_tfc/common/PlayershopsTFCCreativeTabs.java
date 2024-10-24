package net.jotred.playershops_tfc.common;

import net.dries007.tfc.common.blocks.wood.Wood;
import net.jotred.playershops_tfc.common.blocks.PlayershopsTFCBlocks;
import net.jotred.playershops_tfc.common.items.PlayershopsAFCItems;
import net.jotred.playershops_tfc.common.items.PlayershopsTFCItems;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.fml.ModList;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;

import java.util.function.Supplier;


public class PlayershopsTFCCreativeTabs {
	
	public static final DeferredRegister<CreativeModeTab> CREATIVE_TABS =
			DeferredRegister.create(Registries.CREATIVE_MODE_TAB, "playershops_tfc");
	
	public static final PlayershopsTFCCreativeTabs.CreativeTabHolder PLAYERSHOPS_TFC =
			register("playershops", () -> new ItemStack(PlayershopsTFCBlocks.TFC_WOOD_PLAYER_SHOP_BLOCKS.get(Wood.HICKORY).get()), PlayershopsTFCCreativeTabs::fillTab);
	
	
	private static void fillTab(CreativeModeTab.ItemDisplayParameters parameters, CreativeModeTab.Output out)
	{
		for (RegistryObject<Item> item : PlayershopsTFCItems.ITEMS.getEntries()) {
			out.accept(item.get());
		}
		
		if (ModList.get().isLoaded("afc")) {
			
			for (RegistryObject<Item> item : PlayershopsAFCItems.ITEMS_AFC.getEntries()) {
				out.accept(item.get());
			}
		}
	}
	
	private static PlayershopsTFCCreativeTabs.CreativeTabHolder register(String name, Supplier<ItemStack> icon, CreativeModeTab.DisplayItemsGenerator displayItems)
	{
		final RegistryObject<CreativeModeTab> reg = CREATIVE_TABS.register(name, () -> CreativeModeTab.builder()
				.icon(icon)
				.title(Component.translatable("playershops_tfc.creative_tab." + name))
				.displayItems(displayItems)
				.build());
		return new PlayershopsTFCCreativeTabs.CreativeTabHolder(reg, displayItems);
	}
	
	
	public record CreativeTabHolder(RegistryObject<CreativeModeTab> tab, CreativeModeTab.DisplayItemsGenerator generator) {}
}
